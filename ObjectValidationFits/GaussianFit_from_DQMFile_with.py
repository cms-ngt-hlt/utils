import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import ROOT
import array
import mplhep as hep
plt.style.use(hep.style.CMS)

def findBestGaussianCoreFit(histo, quiet=True):
    if not histo or histo.GetEntries() == 0:
        print(f"Histogram '{histo.GetName()}' is empty, skipping fit.")
        return None
    mean, rms = histo.GetMean(), histo.GetRMS()

    gausTF1 = ROOT.TF1()

    RangeLow = mean - 3.0*rms
    RangeUp = mean + 3.0*rms

    histo.Fit("gaus", "0Q", "0", RangeLow, RangeUp)
    gausTF1 = histo.GetListOfFunctions().FindObject("gaus")
    if not gausTF1:
        print(f"Gaussian fit failed for '{histo.GetName()}'.")
        return
    ChiSquare = gausTF1.GetChisquare()
    ndf       = gausTF1.GetNDF()
    Pvalue = ROOT.TMath.Prob(ChiSquare, ndf)

    # if not quiet:
    #     print("\n\nFirst fit in range : [Mean - 2*sigma,  Mean + 2*sigma ] ")
    #     print("ChiSquare = " + str(ChiSquare) + " NDF = " + str(ndf) + " Prob =  " + str(Pvalue))

    RangeLow = gausTF1.GetParameter(1) - 2.0*abs(gausTF1.GetParameter(2))
    RangeUp = gausTF1.GetParameter(1) + 2.0*abs(gausTF1.GetParameter(2))
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

colors = [ "#3f8fda", "#ffa90e", "#832db6", "#bd1f01", "#94a4a2", "#a96b59", "#e76300", "#b9ac70", "#717581", "#92dadd",]
markers = [ "o", "s", "d", "D"]
def plot_histogram_data(ax, bin_centers, bin_contents, bin_errors, bin_edges, 
                       label, color_idx):

    yerr = bin_errors
    ax.errorbar(
        bin_centers,
        bin_contents,
        yerr=yerr,
        label=label,
        color=colors[color_idx % len(colors)],
        fmt=markers[color_idx % len(markers)],
        markersize=5,
        capsize=2,
        linewidth=1.5,
    )
    bin_contents_plus1 = np.append(bin_contents, bin_contents[-1])
    ax.step(
        bin_edges, 
        bin_contents_plus1, 
        where="post", 
        color=colors[color_idx % len(colors)]
    )

def plot_comparison(x_min=None, x_max=None, x_rescale=False, fit=True):
    print(f"\n{output_path}")
    fig, ax_main = plt.subplots(figsize=(size_x,size_y))
    hep.cms.label('Preliminary', rlabel=r'$t\bar{t}+200PU$ (14 TeV)', fontsize=fontsize+1)
    max_ = 0
    for i, num in enumerate([1,4,2,3]):
        file = f'/data/evernazz/NanoAOD/2026_01_12/CMSSW_16_0_0_pre4/src/AAA_Test/TTbar_200PU/NGTScouting{num}/DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root'
        root_hist = CheckRootFile(file, f"{dqm_dir}", rebin=rebin, normalize=normalize)
        gausTF1 = findBestGaussianCoreFit(root_hist, quiet=False)
        xfunc = np.linspace(gausTF1.GetParameter(1) - 2*abs(gausTF1.GetParameter(2)), gausTF1.GetParameter(1) + 2*abs(gausTF1.GetParameter(2)))
        yfunc = np.array([gausTF1.Eval(xi) for xi in xfunc])
        bin_centers, bin_contents, bin_errors, bin_edges, bin_labels, has_labels = (root_to_numpy(root_hist))
        max_ = max_ if max_ > max(bin_contents) else max(bin_contents)
        label = rf'{labels[i]}'
        if fit:
            mu = f"{gausTF1.GetParameter(1)*10000:.2f}" if x_rescale else f"{gausTF1.GetParameter(1):.2f}"
            if mu.startswith("-0.00"):
                mu = mu.replace("-0.00", "0.00")
            if x_rescale:
                label += f' : $\mu={{{mu}}}\pm{{{gausTF1.GetParError(1)*10000:.2f}}}$, $\sigma={{{gausTF1.GetParameter(2)*10000:.2f}}}\pm{{{gausTF1.GetParError(2)*10000:.2f}}}$ [$\mu m$]'
            else:
                label += f' : $\mu={{{mu}}}\pm{{{gausTF1.GetParError(1):.2f}}}$, $\sigma={{{gausTF1.GetParameter(2):.2f}}}\pm{{{gausTF1.GetParError(2):.2f}}}$'
        plot_histogram_data(ax_main, bin_centers, bin_contents, bin_errors, bin_edges, label, i)
        if fit:
            ax_main.plot(xfunc, yfunc, color=colors[i], linewidth=2, linestyle='--')
    ax_main.legend(fontsize=fontsize-3, loc='upper left', title='HLT DA Primary Vertices Performance', title_fontsize=fontsize-1, alignment='left')
    ax_main.set_xlabel(x_title)
    ax_main.set_ylabel(y_title)
    ax_main.set_ylim(0, y_max)
    if x_min is not None and x_max is not None:
        ax_main.set_xlim(x_min, x_max)
    if x_rescale:
        plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands))
    ax_main.grid(True, alpha=0.75, linestyle="dashdot", linewidth=0.75)
    plt.savefig(output_path+'.png', dpi=300, bbox_inches="tight")
    plt.savefig(output_path+'.pdf', dpi=300, bbox_inches="tight")

def thousands(x, pos):
    return f"{x*10000:.0f}"

fontsize = 18; size_x = 9; size_y = 9
labels = ['Legacy', 'Patatrack', 'Ext. Patatrack+LST+MkFit','Ext. Patatrack']

def get_pull_x_title(dim):
    return f"$({dim}^{{\mathrm{{sim}}}} - {dim}^{{\mathrm{{reco}}}})/\delta {dim}^{{\mathrm{{reco}}}}$"

def get_res_x_title(dim):
    return f"${dim}^{{\mathrm{{sim}}}} - {dim}^{{\mathrm{{reco}}}}$ [$\mu m$]"

for dim in ['X', 'Y', 'Z']:
    
    # # Comparison pull
    # rebin = 2; y_max = 800; normalize=False
    # # rebin = 2; y_max = 100; normalize=False
    # dqm_dir = f'DQMData/Run 1/HLT/Run summary/Vertexing/hltFullVertices/Resolution/PV/pull_{dim.lower()}'
    # x_title = f'Pull {dim.lower()} [cm]'
    # y_title = '# Primary Vertices'
    # output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithNewTrackingBaseline/TTbar200PU_Validation_Vertices/Pull{dim}_GaussianFit'
    # plot_comparison(x_min=-4.5, x_max=4.5)

    # Comparison pull wrt sim
    rebin = None; y_max = 900; normalize=False
    dqm_dir = f'DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoPVAssoc2GenPVMatched_Pull{dim}'
    x_title = get_pull_x_title(dim.lower())
    y_title = '# Primary Vertices'
    output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithNewTrackingBaseline/TTbar200PU_Validation_Vertices/Pull{dim}_GaussianFit_Sim'
    plot_comparison(x_min=-4.5, x_max=4.5)

    # # Comparison resolution
    # rebin = None; y_max = 2500; normalize=False
    # dqm_dir = f'DQMData/Run 1/HLT/Run summary/Vertexing/hltFullVertices/Resolution/PV/res_{dim.lower()}'
    # x_title = f'Resolution {dim.lower()} [$\mu m$]'
    # y_title = '# Primary Vertices'
    # output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithNewTrackingBaseline/TTbar200PU_Validation_Vertices/Res{dim}_GaussianFit'
    # plot_comparison(x_min=-0.005, x_max=0.005, x_rescale=True)

    # Comparison resolution wrt sim
    rebin = None; y_max = 1750; normalize=False
    dqm_dir = f'DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoPVAssoc2GenPVMatched_Resol{dim}'
    x_title = get_res_x_title(dim.lower())
    y_title = '# Primary Vertices'
    output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithNewTrackingBaseline/TTbar200PU_Validation_Vertices/Res{dim}_GaussianFit_Sim'
    plot_comparison(x_min=-0.005, x_max=0.005, x_rescale=True)


# rebin = None; y_max = 3000; normalize=False
# dqm_dir = f'DQMData/Run 1/HLT/Run summary/Vertexing/ValidationWRTReconstructableSim/hltOfflinePrimaryVertices/RecoPVAssoc2GenPVMatched_ResolPt2'
# x_title = f'Resolution $\Sigma p_T^2$'
# y_title = '# Primary Vertices'
# output_path = f'/eos/user/e/evernazz/www/NGT/Scouting/DPNotePlots/WithNewTrackingBaseline/TTbar200PU_Validation_Vertices/ResPt2_GaussianFit_Sim'
# plot_comparison(x_min=-2, x_max=2, fit=False)