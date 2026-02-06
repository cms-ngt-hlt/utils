import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.gridspec as gridspec
import numpy as np
import ROOT
import array
import mplhep as hep
plt.style.use(hep.style.CMS)

def define_bins(h):
    """
    Computes the number of bins, edges, centers and widths of a histogram.
    """
    N = h.GetNbinsX()
    edges = np.array([h.GetBinLowEdge(i+1) for i in range(N)])
    edges = np.append(edges, h.GetBinLowEdge(N+1))
    return N, edges, 0.5*(edges[:-1]+edges[1:]), np.diff(edges)

def define_bins_2D(h):
    Nx = h.GetNbinsX()
    Ny = h.GetNbinsY()
    
    x_edges = np.array([h.GetXaxis().GetBinLowEdge(i+1) for i in range(Nx)])
    x_edges = np.append(x_edges, h.GetXaxis().GetBinUpEdge(Nx))
    
    y_edges = np.array([h.GetYaxis().GetBinLowEdge(j+1) for j in range(Ny)])
    y_edges = np.append(y_edges, h.GetYaxis().GetBinUpEdge(Ny))

    return Nx, Ny, x_edges, y_edges

def histo_values_errors(h):
    N = h.GetNbinsX()
    values = np.array([h.GetBinContent(i+1) for i in range(N)])
    errors = np.array([h.GetBinError(i+1) for i in range(N)])
    return values, errors

def histo_values_2D(h, error=False):
    Nx = h.GetNbinsX()
    Ny = h.GetNbinsY()
    values = np.array([
        [h.GetBinContent(i+1, j+1) for i in range(Nx)]
        for j in range(Ny)
    ])
    return values

def findBestGaussianCoreFit(histo, range=3, quiet=True):
    if not histo or histo.GetEntries() == 0:
        print(f"Histogram '{histo.GetName()}' is empty, skipping fit.")
        return None
    mean, rms = histo.GetMean(), histo.GetRMS()

    gausTF1 = ROOT.TF1()

    RangeLow = mean - range*rms
    RangeUp = mean + range*rms

    histo.Fit("gaus", "0Q", "0", RangeLow, RangeUp)
    gausTF1 = histo.GetListOfFunctions().FindObject("gaus")
    if not gausTF1:
        print(f"Gaussian fit failed for '{histo.GetName()}'.")
        return
    ChiSquare = gausTF1.GetChisquare()
    ndf       = gausTF1.GetNDF()
    Pvalue = ROOT.TMath.Prob(ChiSquare, ndf)

    RangeLow = gausTF1.GetParameter(1) - range*abs(gausTF1.GetParameter(2))
    RangeUp = gausTF1.GetParameter(1) + range*abs(gausTF1.GetParameter(2))
    histo.Fit("gaus", "0Q", "0", RangeLow, RangeUp)
    gausTF1 = histo.GetListOfFunctions().FindObject("gaus")
    if not gausTF1:
        print(f"Gaussian fit failed for '{histo.GetName()}'.")
        return
    ChiSquare = gausTF1.GetChisquare()
    ndf       = gausTF1.GetNDF()
    Pvalue = ROOT.TMath.Prob(ChiSquare, ndf)

    if not quiet:
        print("Second fit in range : [Mean - 1*sigma,  Mean + 1*sigma ] ")
        print("ChiSquare = " + str(ChiSquare) + " NDF = " + str(ndf) + " ChiSquare Reduced = " + str(ChiSquare/ndf) + " Prob =  " + str(Pvalue))
    
    return histo.GetListOfFunctions().FindObject("gaus")

def CheckRootFile(file, hname, rebin=None, normalize=None):
    f = ROOT.TFile.Open(file)
    hist_orig = f.Get(hname)
    if not hist_orig:
        print(f"WARNING: Histogram {hname} not found.")
        return None

    safe_base = hist_orig.GetName().replace("/", "_").replace(" ", "_")

    hist = hist_orig.Clone(safe_base + "_clone")
    hist.SetDirectory(0)

    if rebin is not None:
        if isinstance(rebin, (int, float)):
            hist = hist.Rebin(int(rebin), safe_base + "_rebin")
            hist.SetDirectory(0)  # important after Rebin
        elif hasattr(rebin, "__iter__"):
            bin_edges_c = array.array("d", rebin)
            hist = hist.Rebin(len(bin_edges_c) - 1, safe_base + "_rebin", bin_edges_c)
            hist.SetDirectory(0)
        else:
            raise ValueError(f"Unknown type for rebin: {type(rebin)}")

    if normalize:
        integral = hist.Integral()
        if integral > 0:
            hist.Scale(1.0 / integral)

    f.Close()
    return hist

def root_to_numpy(hist):

    n_bins = hist.GetNbinsX()
    bin_edges = np.array([hist.GetBinLowEdge(i) for i in range(1, n_bins + 2)])
    bin_centers = np.array([hist.GetBinCenter(i) for i in range(1, n_bins + 1)])

    bin_contents = np.array([hist.GetBinContent(i) for i in range(1, n_bins + 1)])
    bin_errors = np.array([hist.GetBinError(i) for i in range(1, n_bins + 1)])

    bin_labels = []
    for i in range(1, n_bins + 1):
        label = hist.GetXaxis().GetBinLabel(i)
        bin_labels.append(self._clean_bin_label(label) if label else "")

    # Only use extracted labels if meaningful
    has_labels = any(label and not label.isdigit() for label in bin_labels)

    return bin_centers, bin_contents, bin_errors, bin_edges, bin_labels, has_labels

cmap_eta = plt.cm.viridis
eta_colors = [cmap_eta(i / 100) for i in range(100)]
pt_colors = [ "#bd1f01",  "#e76300", "#ffa90e", "#27d452", "#24580f", "#3fdab3", "#3f8fda", "#2942b2", 
             "#041769", "#33023A", "#9111A5", "#de3f9c"]
colors = [ "#3f8fda", "#ffa90e", "#bd1f01"]
markers = [ "o", "s", "D", "p"]
fontsize = 18; size_x = 9; size_y = 9
labels = ['Legacy', 'Patatrack Patatrack', 'Extended Patatrack']

def plot_response(x_min=None, x_max=None, type='Pt', bins=None, range=3, region=None, output=None):

    mean_vals = []
    mean_errs = []
    sigma_vals = []
    sigma_errs = []
    chi2_vals = []
    for i, num in enumerate([1,2,3]):
        mean_vals.append([])
        mean_errs.append([])
        sigma_vals.append([])
        sigma_errs.append([])
        chi2_vals.append([])
        file = f'/data/evernazz/NanoAOD/2026_01_12/CMSSW_16_0_0_pre4/src/AAA_Test/QCD_200PU/NGTScouting{num}/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root'
        root_hist = CheckRootFile(file, f"{dqm_dir}", rebin=None, normalize=False)
        hep.cms.label('Preliminary', rlabel=r'$QCD+200PU$ (14 TeV)', fontsize=fontsize+1)
        fig, ax_main = plt.subplots(figsize=(size_x,size_y))
        y_max = 0

        for ipt, (low,high) in enumerate(zip(bins[:-1],bins[1:])):
            if root_hist.GetXaxis().FindBin(low) <= 0 and root_hist.GetXaxis().FindBin(high) >= root_hist.GetNbinsX():
                mess = f"Low bin: {low} | Low value: {root_hist.GetXaxis().FindBin(low)} | High bin: {high} | High value: {root_hist.GetXaxis().FindBin(high)}"
                raise RuntimeError(mess)

            # plot individual projection
            hproj = root_hist.ProjectionY(root_hist.GetName() + "_proj" + str(ipt),
                                          root_hist.GetXaxis().FindBin(low), root_hist.GetXaxis().FindBin(high), "e")
            integral = hproj.Integral()
            if integral > 0:
                hproj.Scale(1.0 / integral)
            nbins, bin_edges, bin_centers, bin_widths = define_bins(hproj)
            values, errors = histo_values_errors(hproj)
            y_max = max(y_max, max(values))

            if type == 'Pt':
                colors = pt_colors
                label = str(low) + " < $p_T$ < " + str(high) + " GeV"
            else:
                colors = eta_colors
                label = str(low) + " < $|\\eta|$ < " + str(high)

            # plot gaussian core fit
            gausTF1 = findBestGaussianCoreFit(hproj, range=range, quiet=False)
            if gausTF1:
                xfunc = np.linspace(gausTF1.GetParameter(1) - range*abs(gausTF1.GetParameter(2)), gausTF1.GetParameter(1) + range*abs(gausTF1.GetParameter(2)))
                yfunc = np.array([gausTF1.Eval(xi) for xi in xfunc])
                mu = f"{gausTF1.GetParameter(1):.2f}"; mu = mu.replace("-0.00", "0.00")
                sigma = f"{abs(gausTF1.GetParameter(2)):.2f}"
                chi2_reduced = gausTF1.GetChisquare()/gausTF1.GetNDF() if gausTF1.GetNDF()>0 else -1
                label += f' : $\mu={{{mu}}}\pm{{{gausTF1.GetParError(1)*10000:.2f}}}$, $\sigma={{{sigma}}}\pm{{{gausTF1.GetParError(2):.2f}}}$ ($\chi^2/ndf={{{chi2_reduced:.2f}}}$)'
            else:
                mean_vals[i].append(0)
                mean_errs[i].append(0)
                sigma_vals[i].append(0)
                sigma_errs[i].append(0)
                chi2_vals[i].append(0)
         
            ax_main.errorbar(bin_centers, values, xerr=None, yerr=errors/2, fmt='o', markersize=3, color=colors[ipt], label=label)
            bin_contents_plus1 = np.append(values, values[-1])
            ax_main.step(bin_edges, bin_contents_plus1, where="post", color=colors[ipt])
            ax_main.plot(xfunc, yfunc, color=colors[ipt], linewidth=2, linestyle='--')

            mean_vals[i].append(gausTF1.GetParameter(1))
            mean_errs[i].append(gausTF1.GetParError(1))
            sigma_vals[i].append(abs(gausTF1.GetParameter(2)))
            sigma_errs[i].append(gausTF1.GetParError(2))
            chi2_vals[i].append(chi2_reduced)
        
        legend_title = f'{jet_type} - {labels[i]}' 
        if region: 
            legend_title += f' - {region}'
        ax_main.legend(fontsize=fontsize-4, loc='upper left', title=legend_title, title_fontsize=fontsize-4, alignment='left')
        ax_main.set_xlabel(x_title)
        ax_main.set_ylabel(y_title)
        ax_main.set_ylim(0, 1.5*y_max)
        if x_min is not None and x_max is not None:
            ax_main.set_xlim(x_min, x_max)
        ax_main.grid(True, alpha=0.75, linestyle="dashdot", linewidth=0.75)
        print(f'\n{output}_{num}')
        plt.savefig(output+f'_{num}.png', dpi=300, bbox_inches="tight")
        plt.savefig(output+f'_{num}.pdf', dpi=300, bbox_inches="tight")
        plt.close()

    return mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals

def plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Resolution', region=None, output=None, ymin=None, ymax=None, ymin_ratio=None, ymax_ratio=None):
    fig = plt.figure(figsize=(12, 9))
    gs = gridspec.GridSpec(2, 1, height_ratios=[1 - 0.3, 0.3], hspace=0.10)
    ax_main = fig.add_subplot(gs[0])
    ax_ratio = fig.add_subplot(gs[1], sharex=ax_main)
    hep.cms.label('Preliminary', rlabel=r'$QCD+200PU$ (14 TeV)', fontsize=26, ax=ax_main)
    for i in range(3):
        bin_centers = 0.5 * (bins[:-1] + bins[1:])
        if type == 'Resolution':
            bin_contents = [s/m if m != 0 else 0 for s, m in zip(sigma_vals[i], mean_vals[i])]
            yerr = [np.abs(s_err/m) if m != 0 else 0 for s_err, m in zip(sigma_errs[i], mean_vals[i])]
        elif type == 'Scale':
            bin_contents = mean_vals[i]
            yerr = mean_errs[i]
        ax_main.errorbar(bin_centers, bin_contents, yerr=yerr, label=labels[i], color=colors[i], fmt=markers[i], markersize=5, capsize=2, linewidth=1.5)
        bin_contents_plus1 = np.append(bin_contents, bin_contents[-1])
        ax_main.step(bins, bin_contents_plus1, where="post", color=colors[i])
        if i == 0:
            base_contents = bin_contents
            base_yerr = yerr
    if xbin == 'Pt':
        ax_ratio.set_xlabel(r"$p_{\mathrm{T}}^{\mathrm{gen}}$ [GeV]", fontsize=26)
    elif xbin == 'Eta':
        ax_ratio.set_xlabel(r"$\eta^{\mathrm{gen}}$", fontsize=26)
    if type == 'Resolution':
        if 'RecoOverGen' in dqm_dir:
            ax_main.set_ylabel(r'$\sigma$($p_{\mathrm{T}}^{\mathrm{reco}}/p_{\mathrm{T}}^{\mathrm{gen}}$)/<$p_{\mathrm{T}}^{\mathrm{reco}}/p_{\mathrm{T}}^{\mathrm{gen}}$>',
                               fontsize=26)
        else:
            ax_main.set_ylabel(r'$\sigma$($p_{\mathrm{T}}^{\mathrm{corr}}/p_{\mathrm{T}}^{\mathrm{gen}}$)/<$p_{\mathrm{T}}^{\mathrm{corr}}/p_{\mathrm{T}}^{\mathrm{gen}}$>',
                               fontsize=26)
        print(f'ymin: {ymin}, ymax: {ymax}')
        ax_main.set_ylim(ymin if ymin is not None else 0, ymax if ymax is not None else 0.5)
    elif type == 'Scale':
        if 'RecoOverGen' in dqm_dir:
            ax_main.set_ylabel(r'<$p_{\mathrm{T}}^{\mathrm{reco}}/p_{\mathrm{T}}^{\mathrm{gen}}$>',
                               fontsize=26)
        else:
            ax_main.set_ylabel(r'<$p_{\mathrm{T}}^{\mathrm{corr}}/p_{\mathrm{T}}^{\mathrm{gen}}$>',
                                fontsize=26)
        ax_main.set_ylim(ymin if ymin is not None else 0, ymax if ymax is not None else 2)
        ax_main.axhline(1.0, color='black', linestyle='--', linewidth=1)
    legend_title = f'{jet_type}'
    if region: 
        legend_title += f' - {region}'
    ax_main.legend(fontsize=20, ncols=3, loc='upper center', title=legend_title, title_fontsize=20)
    ax_main.grid(True, alpha=0.75, linestyle="dashdot", linewidth=0.75)
    ax_main.set_xlim(bins[0], bins[-1])
    ax_main.set_xlabel("")
    ax_main.tick_params(axis="x", labelbottom=False)
    for i in range(1, 3):
        bin_centers = 0.5 * (bins[:-1] + bins[1:])
        if type == 'Resolution':
            bin_contents = [s/m if m != 0 else 0 for s, m in zip(sigma_vals[i], mean_vals[i])]
            yerr = [s_err/m if m != 0 else 0 for s_err, m in zip(sigma_errs[i], mean_vals[i])]
        elif type == 'Scale':
            bin_contents = mean_vals[i]
            yerr = mean_errs[i]
        ratio = np.array([a/b if b != 0 else 0 for a, b in zip(bin_contents, base_contents)])
        ratio_err = np.array([np.sqrt((a/b)**2 * ((ea/a)**2 + (eb/b)**2) if a != 0 and b != 0 else 0) for a, b, ea, eb in zip(bin_contents, base_contents, yerr, base_yerr)])
        if len(ratio) != len(ratio_err):
            print(f"Ratio: {ratio}")
            print(f"Ratio error: {ratio_err}")
            print(f"Length mismatch: ratio length {len(ratio)}, ratio_err length {len(ratio_err)}")
        ax_ratio.errorbar(bin_centers, ratio, yerr=ratio_err, label=f'{labels[i]}/{labels[0]}', color=colors[i], fmt=markers[i], markersize=5, capsize=2, linewidth=1.5)
        bin_contents_plus1 = np.append(ratio, ratio[-1])
        ax_ratio.step(bins, bin_contents_plus1, where="post", color=colors[i])
    ax_ratio.set_ylabel('Ratio')
    ax_ratio.set_ylim(ymin_ratio if ymin_ratio is not None else 0.8, ymax_ratio if ymax_ratio is not None else 1.2)
    ax_ratio.grid(True, alpha=0.75, linestyle="dashdot", linewidth=0.75)
    ax_ratio.axhline(1.0, color='black', linestyle='--', linewidth=1)
    print(f'\n{output}')
    plt.savefig(f'{output}.png', dpi=300, bbox_inches="tight")
    plt.savefig(f'{output}.pdf', dpi=300, bbox_inches="tight")
    plt.close()

####################################################################
####################################################################
# PF Puppi Jets Corrected
####################################################################
####################################################################

# Pt dependence

output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/QCD200PU_Validation_PFPuppiJets_Corrected/'
jet_type = 'HLT PF Puppi Jets Corrected'
x_title = r"$p_{\mathrm{T}}^{\mathrm{corr}}/p_{\mathrm{T}}^{\mathrm{gen}}$"
y_title = f'Entries'

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtCorrOverGen_GenPt_B'
output_name = output_path + f'Response_PtBins_Barrel'
bins = np.array((20, 40, 60, 80, 120, 160, 200, 300, 400, 500, 600, 1000))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_B'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Barrel (|$\eta$| < 1.5)', output=output_name, ymin=0.0, ymax=0.4, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_B'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Barrel (|$\eta$| < 1.5)', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtCorrOverGen_GenPt_E'
output_name = output_path + f'Response_PtBins_Endcap'
bins = np.array((20, 40, 60, 80, 120, 160, 200, 300, 400, 500, 600, 1000))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_E'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Endcap (1.5 < |$\eta$| < 3)', output=output_name, ymin=0.0, ymax=0.4, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_E'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Endcap (1.5 < |$\eta$| < 3)', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtCorrOverGen_GenPt_F'
output_name = output_path + f'Response_PtBins_Forward'
bins = np.array((20, 40, 60, 80, 100, 200))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_F'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Forward (|$\eta$| > 3)', output=output_name, ymin=0.0, ymax=0.8, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_F'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Forward (|$\eta$| > 3)', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)

# Eta dependence

x_title = r"$p_{\mathrm{T}}^{\mathrm{corr}}/p_{\mathrm{T}}^{\mathrm{gen}}$"
y_title = f'Entries'
dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtCorrOverGen_GenEta'
output_name = output_path + f'Response_EtaBins'
# bins = np.array((-6, -3, -1.5, 0, 1.5, 3, 6))
bins = np.array([
-3.9, -3.4,
-3.2, -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4,
-1.2, -1.0, -0.8, -0.6, -0.4, -0.2,  0.0,  0.2,  0.4,  0.6,
 0.8,  1.0,  1.2,  1.4,  1.6,  1.8,  2.0,  2.2,  2.4,  2.6,
 2.8,  3.0,  3.2,  3.4,  3.9
])
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Eta', bins=bins, range=1.5, output=output_name)
output_name = output_path + f'Resolution_vs_GenEta'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Eta',type='Resolution', output=output_name, ymin=0.0, ymax=0.7, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenEta'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Eta', type='Scale', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)

####################################################################
####################################################################
# PF Jets
####################################################################
####################################################################

# Pt dependence

output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/QCD200PU_Validation_PFJets/'
jet_type = 'HLT PF Jets'
x_title = r"$p_{\mathrm{T}}^{\mathrm{reco}}/p_{\mathrm{T}}^{\mathrm{gen}}$"
y_title = f'Entries'

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFJets/h2d_PtRecoOverGen_GenPt_B'
output_name = output_path + f'Response_PtBins_Barrel'
bins = np.array((20, 40, 60, 80, 120, 160, 200, 300, 400, 500, 600, 1000))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_B'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Barrel (|$\eta$| < 1.5)', output=output_name, ymin=0.0, ymax=0.5, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_B'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Barrel (|$\eta$| < 1.5)', output=output_name, ymin=0.0, ymax=3.5, ymin_ratio=0.8, ymax_ratio=1.2)

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFJets/h2d_PtRecoOverGen_GenPt_E'
output_name = output_path + f'Response_PtBins_Endcap'
bins = np.array((20, 40, 60, 80, 120, 160, 200, 300, 400, 500, 600, 1000))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_E'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Endcap (1.5 < |$\eta$| < 3)', output=output_name, ymin=0.0, ymax=0.5, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_E'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Endcap (1.5 < |$\eta$| < 3)', output=output_name, ymin=0.0, ymax=3.5, ymin_ratio=0.8, ymax_ratio=1.2)

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFJets/h2d_PtRecoOverGen_GenPt_F'
output_name = output_path + f'Response_PtBins_Forward'
bins = np.array((20, 40, 60, 80, 100, 200))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_F'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Forward (|$\eta$| > 3)', output=output_name, ymin=0.0, ymax=0.8, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_F'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Forward (|$\eta$| > 3)', output=output_name, ymin=0.0, ymax=3.5, ymin_ratio=0.8, ymax_ratio=1.2)

# Eta dependence

x_title = r"$p_{\mathrm{T}}^{\mathrm{reco}}/p_{\mathrm{T}}^{\mathrm{gen}}$"
y_title = f'Entries'
dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFJets/h2d_PtRecoOverGen_GenEta'
output_name = output_path + f'Response_EtaBins'
# bins = np.array((-6, -3, -1.5, 0, 1.5, 3, 6))
bins = np.array([
-3.9, -3.4,
-3.2, -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4,
-1.2, -1.0, -0.8, -0.6, -0.4, -0.2,  0.0,  0.2,  0.4,  0.6,
 0.8,  1.0,  1.2,  1.4,  1.6,  1.8,  2.0,  2.2,  2.4,  2.6,
 2.8,  3.0,  3.2,  3.4,  3.9
])
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Eta', bins=bins, range=1.5, output=output_name)
output_name = output_path + f'Resolution_vs_GenEta'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Eta',type='Resolution', output=output_name, ymin=0.0, ymax=0.8, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenEta'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Eta', type='Scale', output=output_name, ymin=0.0, ymax=3.5, ymin_ratio=0.8, ymax_ratio=1.2)

####################################################################
####################################################################
# PF Puppi Jets
####################################################################
####################################################################

# Pt dependence

output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithoutNewTrackingBaseline/QCD200PU_Validation_PFPuppiJets/'
jet_type = 'HLT PF Puppi Jets'
x_title = r"$p_{\mathrm{T}}^{\mathrm{reco}}/p_{\mathrm{T}}^{\mathrm{gen}}$"
y_title = f'Entries'

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtRecoOverGen_GenPt_B'
output_name = output_path + f'Response_PtBins_Barrel'
bins = np.array((20, 40, 60, 80, 120, 160, 200, 300, 400, 500, 600, 1000))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_B'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Barrel (|$\eta$| < 1.5)', output=output_name, ymin=0.0, ymax=0.4, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_B'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Barrel (|$\eta$| < 1.5)', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtRecoOverGen_GenPt_E'
output_name = output_path + f'Response_PtBins_Endcap'
bins = np.array((20, 40, 60, 80, 120, 160, 200, 300, 400, 500, 600, 1000))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_E'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Endcap (1.5 < |$\eta$| < 3)', output=output_name, ymin=0.0, ymax=0.4, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_E'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Endcap (1.5 < |$\eta$| < 3)', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)

dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtRecoOverGen_GenPt_F'
output_name = output_path + f'Response_PtBins_Forward'
bins = np.array((20, 40, 60, 80, 100, 200))
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Pt', bins=bins, range=3, output=output_name)
output_name = output_path + f'Resolution_vs_GenPt_F'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, type='Resolution', region='Forward (|$\eta$| > 3)', output=output_name, ymin=0.0, ymax=0.8, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenPt_F'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Pt', type='Scale', region='Forward (|$\eta$| > 3)', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)

# Eta dependence

x_title = r"$p_{\mathrm{T}}^{\mathrm{reco}}/p_{\mathrm{T}}^{\mathrm{gen}}$"
y_title = f'Entries'
dqm_dir = f'DQMData/Run 1/HLT/Run summary/JetMET/JetValidation/hltAK4PFPuppiJets/h2d_PtRecoOverGen_GenEta'
output_name = output_path + f'Response_EtaBins'
# bins = np.array((-6, -3, -1.5, 0, 1.5, 3, 6))
bins = np.array([
-4, -3.5, -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4,
-1.2, -1.0, -0.8, -0.6, -0.4, -0.2,  0.0,  0.2,  0.4,  0.6,
 0.8,  1.0,  1.2,  1.4,  1.6,  1.8,  2.0,  2.2,  2.4,  2.6,
 2.8,  3.0, 3.5,  4.0
])
mean_vals, mean_errs, sigma_vals, sigma_errs, chi2_vals = plot_response(x_min=0.0, x_max=2.0, type='Eta', bins=bins, range=1.6, output=output_name)
output_name = output_path + f'Resolution_vs_GenEta'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Eta',type='Resolution', output=output_name, ymin=0.0, ymax=0.7, ymin_ratio=0.5, ymax_ratio=1.5)
output_name = output_path + f'Scale_vs_GenEta'
plot_comparison(bins, mean_vals, mean_errs, sigma_vals, sigma_errs, xbin='Eta', type='Scale', output=output_name, ymin_ratio=0.8, ymax_ratio=1.2)
