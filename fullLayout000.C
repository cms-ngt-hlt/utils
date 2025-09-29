#ifdef __CLING__
#pragma cling optimize(0)
#endif
void fullLayout000()
{
//=========Macro generated from canvas: fullLayout000/RZView Canvas (full layout)
//=========  (Fri Aug 29 15:51:06 2025) by ROOT version 6.34.08
   TCanvas *fullLayout000 = new TCanvas("fullLayout000", "RZView Canvas (full layout)",3698,406,1804,628);
   fullLayout000->SetHighLightColor(2);
   fullLayout000->Range(-367.625,-151.375,3308.625,1362.375);
   fullLayout000->SetFillColor(0);
   fullLayout000->SetBorderMode(0);
   fullLayout000->SetBorderSize(2);
   fullLayout000->SetFrameBorderMode(0);
   fullLayout000->SetFrameBorderMode(0);
   
   TH2C *Info_fullLayout_frameYZ93__1 = new TH2C("Info_fullLayout_frameYZ93__1","",1000,0,2941,1000,0,1211);
   Info_fullLayout_frameYZ93__1->SetDirectory(nullptr);
   Info_fullLayout_frameYZ93__1->SetStats(0);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#000099");
   Info_fullLayout_frameYZ93__1->SetLineColor(ci);
   Info_fullLayout_frameYZ93__1->GetXaxis()->SetTitle("z [mm]");
   Info_fullLayout_frameYZ93__1->GetXaxis()->SetLabelFont(42);
   Info_fullLayout_frameYZ93__1->GetXaxis()->SetTitleOffset(1.3);
   Info_fullLayout_frameYZ93__1->GetXaxis()->SetTitleFont(42);
   Info_fullLayout_frameYZ93__1->GetYaxis()->SetTitle("r [mm]");
   Info_fullLayout_frameYZ93__1->GetYaxis()->SetLabelFont(42);
   Info_fullLayout_frameYZ93__1->GetYaxis()->SetTitleFont(42);
   Info_fullLayout_frameYZ93__1->GetZaxis()->SetLabelFont(42);
   Info_fullLayout_frameYZ93__1->GetZaxis()->SetTitleOffset(1);
   Info_fullLayout_frameYZ93__1->GetZaxis()->SetTitleFont(42);
   Info_fullLayout_frameYZ93__1->Draw("");
   TLine *line = new TLine(7.415236e-14,1211,7.711846e-14,1259.44);
   line->Draw();
   TText *text = new TText(8.008455e-14,1307.88,"0.0");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(243.8179,1211,253.5706,1259.44);
   line->Draw();
   text = new TText(263.3233,1307.88,"0.2");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(497.4211,1211,517.3179,1259.44);
   line->Draw();
   text = new TText(537.2148,1307.88,"0.4");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(770.9875,1211,801.827,1259.44);
   line->Draw();
   text = new TText(832.6665,1307.88,"0.6");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(1075.496,1211,1118.516,1259.44);
   line->Draw();
   text = new TText(1161.536,1307.88,"0.8");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(1423.169,1211,1480.095,1259.44);
   line->Draw();
   text = new TText(1537.022,1307.88,"1.0");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(1827.958,1211,1901.076,1259.44);
   line->Draw();
   text = new TText(1974.194,1307.88,"1.2");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2306.109,1211,2398.353,1259.44);
   line->Draw();
   text = new TText(2490.598,1307.88,"1.4");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2876.813,1211,2991.885,1259.44);
   line->Draw();
   text = new TText(3040.994,1280.112,"1.6");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,999.6009,2990.997,1016.594);
   line->Draw();
   text = new TText(3040.994,1033.587,"1.8");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,810.8942,2990.997,824.6794);
   line->Draw();
   text = new TText(3040.994,838.4646,"2.0");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,659.8453,2990.997,671.0627);
   line->Draw();
   text = new TText(3040.994,682.2801,"2.2");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,538.0309,2990.997,547.1774);
   line->Draw();
   text = new TText(3040.994,556.3239,"2.4");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,439.3006,2990.997,446.7687);
   line->Draw();
   text = new TText(3040.994,454.2368,"2.6");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,359.0124,2990.997,365.1156);
   line->Draw();
   text = new TText(3040.994,371.2188,"2.8");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,293.5752,2990.997,298.566);
   line->Draw();
   text = new TText(3040.994,303.5568,"3.0");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,240.1623,2990.997,244.2451);
   line->Draw();
   text = new TText(3040.994,248.3278,"3.2");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.035);
   text->Draw();
   line = new TLine(2941,107.7687,2990.997,109.6008);
   line->Draw();
   line = new TLine(0,0,2990.997,109.6008);

   ci = TColor::GetColor("#cccccc");
   line->SetLineColor(ci);
   line->Draw();
   text = new TText(3040.994,111.4329,"4.0");
   text->SetTextAlign(21);
   text->SetTextFont(42);
   text->SetTextSize(0.07);
   text->Draw();
   TLatex *   tex = new TLatex(3040.994,-33.88712,"#eta");
   tex->SetTextFont(42);
   tex->SetTextSize(0.07);
   tex->SetLineWidth(2);
   tex->Draw();
   
   TPolyLine *pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,27.5);
   pline->SetPoint(1,21.725,27.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,32.5);
   pline->SetPoint(1,21.725,32.5);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,32.588);
   pline->SetPoint(1,21.725,32.588);
   pline->SetPoint(2,21.725,37.361);
   pline->SetPoint(3,-21.725,37.361);
   pline->SetPoint(4,-21.725,32.588);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,59);
   pline->SetPoint(1,21.725,59);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,64);
   pline->SetPoint(1,21.725,64);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,64.046);
   pline->SetPoint(1,21.725,64.046);
   pline->SetPoint(2,21.725,68.9);
   pline->SetPoint(3,-21.725,68.9);
   pline->SetPoint(4,-21.725,64.046);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,102);
   pline->SetPoint(1,21.725,102);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,107);
   pline->SetPoint(1,21.725,107);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,107.028);
   pline->SetPoint(1,21.725,107.028);
   pline->SetPoint(2,21.725,111.958);
   pline->SetPoint(3,-21.725,111.958);
   pline->SetPoint(4,-21.725,107.028);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,144);
   pline->SetPoint(1,21.725,144);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,149);
   pline->SetPoint(1,21.725,149);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-21.725,149.021);
   pline->SetPoint(1,21.725,149.021);
   pline->SetPoint(2,21.725,153.966);
   pline->SetPoint(3,-21.725,153.966);
   pline->SetPoint(4,-21.725,149.021);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,224.648);
   pline->SetPoint(1,23.472,224.648);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,248.448);
   pline->SetPoint(1,23.472,248.448);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,248.448);
   pline->SetPoint(1,23.472,248.448);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,352.847);
   pline->SetPoint(1,23.472,352.847);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,376.647);
   pline->SetPoint(1,23.472,376.647);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,376.648);
   pline->SetPoint(1,23.472,376.648);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,505.684);
   pline->SetPoint(1,23.472,505.684);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,-23.472,529.484);
   pline->SetPoint(1,23.472,529.484);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,19.461,217.552);
   pline->SetPoint(1,66.405,217.552);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,19.461,217.552);
   pline->SetPoint(1,66.405,217.552);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,19.461,241.353);
   pline->SetPoint(1,66.405,241.353);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,22.325,27.5);
   pline->SetPoint(1,65.775,27.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,22.325,32.5);
   pline->SetPoint(1,65.775,32.5);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,22.325,32.588);
   pline->SetPoint(1,65.775,32.588);
   pline->SetPoint(2,65.775,37.361);
   pline->SetPoint(3,22.325,37.361);
   pline->SetPoint(4,22.325,32.588);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,22.325,59);
   pline->SetPoint(1,65.775,59);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,22.325,64);
   pline->SetPoint(1,65.775,64);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,22.325,64.046);
   pline->SetPoint(1,65.775,64.046);
   pline->SetPoint(2,65.775,68.9);
   pline->SetPoint(3,22.325,68.9);
   pline->SetPoint(4,22.325,64.046);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,23.025,102);
   pline->SetPoint(1,66.475,102);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,23.025,107);
   pline->SetPoint(1,66.475,107);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,23.025,107.028);
   pline->SetPoint(1,66.475,107.028);
   pline->SetPoint(2,66.475,111.958);
   pline->SetPoint(3,23.025,111.958);
   pline->SetPoint(4,23.025,107.028);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,23.025,144);
   pline->SetPoint(1,66.475,144);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,23.025,149);
   pline->SetPoint(1,66.475,149);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,23.025,149.021);
   pline->SetPoint(1,66.475,149.021);
   pline->SetPoint(2,66.475,153.966);
   pline->SetPoint(3,23.025,153.966);
   pline->SetPoint(4,23.025,149.021);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,21.438,346.753);
   pline->SetPoint(1,68.382,346.753);
   pline->SetPoint(2,68.382,346.752);
   pline->SetPoint(3,21.438,346.752);
   pline->SetPoint(4,21.438,346.753);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,21.438,346.753);
   pline->SetPoint(1,68.382,346.753);
   pline->SetPoint(2,68.382,346.752);
   pline->SetPoint(3,21.438,346.752);
   pline->SetPoint(4,21.438,346.753);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,21.438,370.552);
   pline->SetPoint(1,68.382,370.552);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,21.438,370.553);
   pline->SetPoint(1,68.382,370.553);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,21.854,498.516);
   pline->SetPoint(1,68.798,498.516);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,21.854,522.316);
   pline->SetPoint(1,68.798,522.316);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2.55,673.45);
   pline->SetPoint(1,103.05,673.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2.55,705.05);
   pline->SetPoint(1,103.05,705.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2.55,846.45);
   pline->SetPoint(1,103.05,846.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2.55,878.05);
   pline->SetPoint(1,103.05,878.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2.55,1069.45);
   pline->SetPoint(1,103.05,1069.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2.55,1101.05);
   pline->SetPoint(1,103.05,1101.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.375,27.5);
   pline->SetPoint(1,109.825,27.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.375,32.5);
   pline->SetPoint(1,109.825,32.5);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.375,32.588);
   pline->SetPoint(1,109.825,32.588);
   pline->SetPoint(2,109.825,37.361);
   pline->SetPoint(3,66.375,37.361);
   pline->SetPoint(4,66.375,32.588);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.375,59);
   pline->SetPoint(1,109.825,59);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.375,64);
   pline->SetPoint(1,109.825,64);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.375,64.046);
   pline->SetPoint(1,109.825,64.046);
   pline->SetPoint(2,109.825,68.9);
   pline->SetPoint(3,66.375,68.9);
   pline->SetPoint(4,66.375,64.046);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,67.775,102);
   pline->SetPoint(1,111.225,102);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,67.775,107);
   pline->SetPoint(1,111.225,107);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,67.775,107.028);
   pline->SetPoint(1,111.225,107.028);
   pline->SetPoint(2,111.225,111.958);
   pline->SetPoint(3,67.775,111.958);
   pline->SetPoint(4,67.775,107.028);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,67.775,144);
   pline->SetPoint(1,111.225,144);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,67.775,149);
   pline->SetPoint(1,111.225,149);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,67.775,149.021);
   pline->SetPoint(1,111.225,149.021);
   pline->SetPoint(2,111.225,153.966);
   pline->SetPoint(3,67.775,153.966);
   pline->SetPoint(4,67.775,149.021);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.244,224.648);
   pline->SetPoint(1,113.188,224.648);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.244,248.448);
   pline->SetPoint(1,113.188,248.448);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,66.244,248.448);
   pline->SetPoint(1,113.188,248.448);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,68.346,352.847);
   pline->SetPoint(1,115.29,352.847);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,68.346,376.647);
   pline->SetPoint(1,115.29,376.647);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,68.346,376.648);
   pline->SetPoint(1,115.29,376.648);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,68.777,505.684);
   pline->SetPoint(1,115.721,505.684);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,68.777,529.484);
   pline->SetPoint(1,115.721,529.484);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,105.328,217.552);
   pline->SetPoint(1,152.272,217.552);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,105.328,217.552);
   pline->SetPoint(1,152.272,217.552);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,105.328,241.353);
   pline->SetPoint(1,152.272,241.353);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,110.425,27.5);
   pline->SetPoint(1,153.875,27.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,110.425,32.5);
   pline->SetPoint(1,153.875,32.5);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,110.425,32.588);
   pline->SetPoint(1,153.875,32.588);
   pline->SetPoint(2,153.875,37.361);
   pline->SetPoint(3,110.425,37.361);
   pline->SetPoint(4,110.425,32.588);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,110.425,59);
   pline->SetPoint(1,153.875,59);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,110.425,64);
   pline->SetPoint(1,153.875,64);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,110.425,64.046);
   pline->SetPoint(1,153.875,64.046);
   pline->SetPoint(2,153.875,68.9);
   pline->SetPoint(3,110.425,68.9);
   pline->SetPoint(4,110.425,64.046);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.525,102);
   pline->SetPoint(1,155.975,102);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.525,107);
   pline->SetPoint(1,155.975,107);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.525,107.028);
   pline->SetPoint(1,155.975,107.028);
   pline->SetPoint(2,155.975,111.958);
   pline->SetPoint(3,112.525,111.958);
   pline->SetPoint(4,112.525,107.028);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.525,144);
   pline->SetPoint(1,155.975,144);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.525,149);
   pline->SetPoint(1,155.975,149);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.525,149.021);
   pline->SetPoint(1,155.975,149.021);
   pline->SetPoint(2,155.975,153.966);
   pline->SetPoint(3,112.525,153.966);
   pline->SetPoint(4,112.525,149.021);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,111.258,346.753);
   pline->SetPoint(1,158.202,346.753);
   pline->SetPoint(2,158.202,346.752);
   pline->SetPoint(3,111.258,346.752);
   pline->SetPoint(4,111.258,346.753);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,111.258,346.753);
   pline->SetPoint(1,158.202,346.753);
   pline->SetPoint(2,158.202,346.752);
   pline->SetPoint(3,111.258,346.752);
   pline->SetPoint(4,111.258,346.753);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,111.258,370.552);
   pline->SetPoint(1,158.202,370.552);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,111.258,370.553);
   pline->SetPoint(1,158.202,370.553);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.505,498.516);
   pline->SetPoint(1,159.449,498.516);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,112.505,522.316);
   pline->SetPoint(1,159.449,522.316);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,101.434,668.95);
   pline->SetPoint(1,201.934,668.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,101.434,700.55);
   pline->SetPoint(1,201.934,700.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,101.434,841.95);
   pline->SetPoint(1,201.934,841.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,101.434,873.55);
   pline->SetPoint(1,201.934,873.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,101.434,1064.95);
   pline->SetPoint(1,201.934,1064.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,101.434,1096.55);
   pline->SetPoint(1,201.934,1096.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,156.087,269.166);
   pline->SetPoint(1,188.103,234.834);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,154.475,27.5);
   pline->SetPoint(1,197.925,27.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,154.475,32.5);
   pline->SetPoint(1,197.925,32.5);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#333300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,154.475,32.588);
   pline->SetPoint(1,197.925,32.588);
   pline->SetPoint(2,197.925,37.361);
   pline->SetPoint(3,154.475,37.361);
   pline->SetPoint(4,154.475,32.588);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,154.475,59);
   pline->SetPoint(1,197.925,59);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,154.475,64);
   pline->SetPoint(1,197.925,64);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#339900");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,154.475,64.046);
   pline->SetPoint(1,197.925,64.046);
   pline->SetPoint(2,197.925,68.9);
   pline->SetPoint(3,154.475,68.9);
   pline->SetPoint(4,154.475,64.046);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,157.275,102);
   pline->SetPoint(1,200.725,102);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,157.275,107);
   pline->SetPoint(1,200.725,107);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,157.275,107.028);
   pline->SetPoint(1,200.725,107.028);
   pline->SetPoint(2,200.725,111.958);
   pline->SetPoint(3,157.275,111.958);
   pline->SetPoint(4,157.275,107.028);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,157.275,144);
   pline->SetPoint(1,200.725,144);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,157.275,149);
   pline->SetPoint(1,200.725,149);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff9933");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,157.275,149.021);
   pline->SetPoint(1,200.725,149.021);
   pline->SetPoint(2,200.725,153.966);
   pline->SetPoint(3,157.275,153.966);
   pline->SetPoint(4,157.275,149.021);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,165.883,282.166);
   pline->SetPoint(1,197.899,247.834);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,159.27,352.847);
   pline->SetPoint(1,206.214,352.847);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,159.27,376.647);
   pline->SetPoint(1,206.214,376.647);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,159.27,376.648);
   pline->SetPoint(1,206.214,376.648);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,160.401,505.684);
   pline->SetPoint(1,207.345,505.684);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,160.401,529.484);
   pline->SetPoint(1,207.345,529.484);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,201.11,269.166);
   pline->SetPoint(1,233.125,234.834);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,200.204,346.753);
   pline->SetPoint(1,247.148,346.753);
   pline->SetPoint(2,247.148,346.752);
   pline->SetPoint(3,200.204,346.752);
   pline->SetPoint(4,200.204,346.753);
   pline->Draw("");
   
   pline = new TPolyLine(5,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,200.204,346.753);
   pline->SetPoint(1,247.148,346.753);
   pline->SetPoint(2,247.148,346.752);
   pline->SetPoint(3,200.204,346.752);
   pline->SetPoint(4,200.204,346.753);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,200.204,370.552);
   pline->SetPoint(1,247.148,370.552);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,200.204,370.553);
   pline->SetPoint(1,247.148,370.553);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.544,498.516);
   pline->SetPoint(1,249.488,498.516);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.544,522.316);
   pline->SetPoint(1,249.488,522.316);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,210.906,282.166);
   pline->SetPoint(1,242.922,247.834);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,244,92.45);
   pline->SetPoint(1,244,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,244,159.99);
   pline->SetPoint(1,244,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,249.5,92.45);
   pline->SetPoint(1,249.5,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,249.5,159.99);
   pline->SetPoint(1,249.5,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.258,673.45);
   pline->SetPoint(1,302.758,673.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.258,705.05);
   pline->SetPoint(1,302.758,705.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.258,846.45);
   pline->SetPoint(1,302.758,846.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.258,878.05);
   pline->SetPoint(1,302.758,878.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.258,1069.45);
   pline->SetPoint(1,302.758,1069.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,202.258,1101.05);
   pline->SetPoint(1,302.758,1101.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,256.5,74.45);
   pline->SetPoint(1,256.5,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,256.5,126.65);
   pline->SetPoint(1,256.5,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,262,74.45);
   pline->SetPoint(1,262,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,262,126.65);
   pline->SetPoint(1,262,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,251.98,269.166);
   pline->SetPoint(1,283.995,234.834);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,251.907,389.088);
   pline->SetPoint(1,287.869,358.912);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,251.398,505.684);
   pline->SetPoint(1,298.342,505.684);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,251.398,529.484);
   pline->SetPoint(1,298.342,529.484);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,259.413,402.088);
   pline->SetPoint(1,295.374,371.912);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,261.776,282.166);
   pline->SetPoint(1,293.792,247.834);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,313.95,92.45);
   pline->SetPoint(1,313.95,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,313.95,159.99);
   pline->SetPoint(1,313.95,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,303.448,269.327);
   pline->SetPoint(1,326.92,228.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,291.965,498.516);
   pline->SetPoint(1,338.909,498.516);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,291.965,522.316);
   pline->SetPoint(1,338.909,522.316);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,319.45,92.45);
   pline->SetPoint(1,319.45,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,319.45,159.99);
   pline->SetPoint(1,319.45,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,304.002,389.088);
   pline->SetPoint(1,339.963,358.912);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,326.45,74.45);
   pline->SetPoint(1,326.45,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,326.45,126.65);
   pline->SetPoint(1,326.45,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,315.365,279.327);
   pline->SetPoint(1,338.837,238.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,311.507,402.088);
   pline->SetPoint(1,347.468,371.912);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,331.95,74.45);
   pline->SetPoint(1,331.95,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,331.95,126.65);
   pline->SetPoint(1,331.95,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,299.276,668.95);
   pline->SetPoint(1,399.776,668.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,299.276,700.55);
   pline->SetPoint(1,399.776,700.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,299.276,841.95);
   pline->SetPoint(1,399.776,841.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,299.276,873.55);
   pline->SetPoint(1,399.776,873.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,299.276,1064.95);
   pline->SetPoint(1,399.776,1064.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,299.276,1096.55);
   pline->SetPoint(1,399.776,1096.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,346.163,540.805);
   pline->SetPoint(1,379.931,508.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,354.257,552.805);
   pline->SetPoint(1,388.025,520.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,362.467,269.327);
   pline->SetPoint(1,385.939,228.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,360.425,389.088);
   pline->SetPoint(1,396.386,358.912);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,367.931,402.088);
   pline->SetPoint(1,403.892,371.912);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,374.385,279.327);
   pline->SetPoint(1,397.857,238.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,403.23,92.45);
   pline->SetPoint(1,403.23,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,403.23,159.99);
   pline->SetPoint(1,403.23,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,408.73,92.45);
   pline->SetPoint(1,408.73,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,408.73,159.99);
   pline->SetPoint(1,408.73,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,415.73,74.45);
   pline->SetPoint(1,415.73,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,415.73,126.65);
   pline->SetPoint(1,415.73,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,399.268,540.805);
   pline->SetPoint(1,433.036,508.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,421.23,74.45);
   pline->SetPoint(1,421.23,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,421.23,126.65);
   pline->SetPoint(1,421.23,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,407.362,552.805);
   pline->SetPoint(1,441.13,520.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,417.851,391.227);
   pline->SetPoint(1,444.777,352.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,426.851,400.227);
   pline->SetPoint(1,453.777,361.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,431.96,269.327);
   pline->SetPoint(1,455.432,228.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,400.587,673.45);
   pline->SetPoint(1,501.087,673.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,400.587,705.05);
   pline->SetPoint(1,501.087,705.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,400.587,846.45);
   pline->SetPoint(1,501.087,846.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,400.587,878.05);
   pline->SetPoint(1,501.087,878.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,400.587,1069.45);
   pline->SetPoint(1,501.087,1069.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,400.587,1101.05);
   pline->SetPoint(1,501.087,1101.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,443.878,279.327);
   pline->SetPoint(1,467.35,238.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,455.8,540.805);
   pline->SetPoint(1,489.568,508.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,463.894,552.805);
   pline->SetPoint(1,497.662,520.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,482.282,391.227);
   pline->SetPoint(1,509.208,352.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,491.282,400.227);
   pline->SetPoint(1,518.208,361.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,517.2,92.45);
   pline->SetPoint(1,517.2,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,517.2,159.99);
   pline->SetPoint(1,517.2,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,522.7,92.45);
   pline->SetPoint(1,522.7,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,522.7,159.99);
   pline->SetPoint(1,522.7,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,515.036,269.327);
   pline->SetPoint(1,538.508,228.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,529.7,74.45);
   pline->SetPoint(1,529.7,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,529.7,126.65);
   pline->SetPoint(1,529.7,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,516.125,540.805);
   pline->SetPoint(1,549.894,508.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,535.2,74.45);
   pline->SetPoint(1,535.2,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,535.2,126.65);
   pline->SetPoint(1,535.2,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,526.954,279.327);
   pline->SetPoint(1,550.426,238.673);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,524.219,552.805);
   pline->SetPoint(1,557.988,520.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,495.752,668.95);
   pline->SetPoint(1,596.252,668.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,495.752,700.55);
   pline->SetPoint(1,596.252,700.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,495.752,841.95);
   pline->SetPoint(1,596.252,841.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,495.752,873.55);
   pline->SetPoint(1,596.252,873.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,495.752,1064.95);
   pline->SetPoint(1,596.252,1064.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,495.752,1096.55);
   pline->SetPoint(1,596.252,1096.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,553.799,391.227);
   pline->SetPoint(1,580.725,352.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,562.799,400.227);
   pline->SetPoint(1,589.725,361.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,580.352,540.805);
   pline->SetPoint(1,614.12,508.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,588.446,552.805);
   pline->SetPoint(1,622.214,520.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,603.834,272.823);
   pline->SetPoint(1,618.34,228.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,615.118,278.823);
   pline->SetPoint(1,629.624,234.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,632.645,391.227);
   pline->SetPoint(1,659.571,352.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,597.547,673.45);
   pline->SetPoint(1,698.047,673.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,597.547,705.05);
   pline->SetPoint(1,698.047,705.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,597.547,846.45);
   pline->SetPoint(1,698.047,846.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,597.547,878.05);
   pline->SetPoint(1,698.047,878.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,597.547,1069.45);
   pline->SetPoint(1,698.047,1069.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,597.547,1101.05);
   pline->SetPoint(1,698.047,1101.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,641.645,400.227);
   pline->SetPoint(1,668.571,361.773);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,662.68,92.45);
   pline->SetPoint(1,662.68,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,662.68,159.99);
   pline->SetPoint(1,662.68,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,648.224,540.805);
   pline->SetPoint(1,681.993,508.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,668.18,92.45);
   pline->SetPoint(1,668.18,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,668.18,159.99);
   pline->SetPoint(1,668.18,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,656.318,552.805);
   pline->SetPoint(1,690.087,520.195);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,675.18,74.45);
   pline->SetPoint(1,675.18,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,675.18,126.65);
   pline->SetPoint(1,675.18,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,680.68,74.45);
   pline->SetPoint(1,680.68,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,680.68,126.65);
   pline->SetPoint(1,680.68,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,712.993,272.823);
   pline->SetPoint(1,727.499,228.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,716.443,392.763);
   pline->SetPoint(1,734.029,349.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,716.089,542.827);
   pline->SetPoint(1,739.561,502.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,724.277,278.823);
   pline->SetPoint(1,738.784,234.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,727.646,399.763);
   pline->SetPoint(1,745.231,356.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,725.623,550.827);
   pline->SetPoint(1,749.095,510.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,690.547,668.95);
   pline->SetPoint(1,791.047,668.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,690.547,700.55);
   pline->SetPoint(1,791.047,700.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,690.547,841.95);
   pline->SetPoint(1,791.047,841.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,690.547,873.55);
   pline->SetPoint(1,791.047,873.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,690.547,1064.95);
   pline->SetPoint(1,791.047,1064.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,690.547,1096.55);
   pline->SetPoint(1,791.047,1096.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,793.097,542.827);
   pline->SetPoint(1,816.569,502.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,802.631,550.827);
   pline->SetPoint(1,826.103,510.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,811.849,392.763);
   pline->SetPoint(1,829.435,349.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,823.052,399.763);
   pline->SetPoint(1,840.637,356.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,833.38,92.45);
   pline->SetPoint(1,833.38,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,833.38,159.99);
   pline->SetPoint(1,833.38,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,838.88,92.45);
   pline->SetPoint(1,838.88,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,838.88,159.99);
   pline->SetPoint(1,838.88,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,792.821,673.45);
   pline->SetPoint(1,893.321,673.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,792.821,705.05);
   pline->SetPoint(1,893.321,705.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,792.821,846.45);
   pline->SetPoint(1,893.321,846.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,792.821,878.05);
   pline->SetPoint(1,893.321,878.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,792.821,1069.45);
   pline->SetPoint(1,893.321,1069.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,792.821,1101.05);
   pline->SetPoint(1,893.321,1101.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,845.88,74.45);
   pline->SetPoint(1,845.88,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,845.88,126.65);
   pline->SetPoint(1,845.88,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,843.364,272.823);
   pline->SetPoint(1,857.87,228.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,851.38,74.45);
   pline->SetPoint(1,851.38,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,851.38,126.65);
   pline->SetPoint(1,851.38,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,854.648,278.823);
   pline->SetPoint(1,869.155,234.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,876.443,542.827);
   pline->SetPoint(1,899.915,502.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,885.977,550.827);
   pline->SetPoint(1,909.449,510.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,918.803,392.763);
   pline->SetPoint(1,936.388,349.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,883.821,668.95);
   pline->SetPoint(1,984.321,668.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,883.821,700.55);
   pline->SetPoint(1,984.321,700.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,883.821,841.95);
   pline->SetPoint(1,984.321,841.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,883.821,873.55);
   pline->SetPoint(1,984.321,873.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,883.821,1064.95);
   pline->SetPoint(1,984.321,1064.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,883.821,1096.55);
   pline->SetPoint(1,984.321,1096.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,930.005,399.763);
   pline->SetPoint(1,947.591,356.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,966.549,542.827);
   pline->SetPoint(1,990.021,502.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,976.083,550.827);
   pline->SetPoint(1,999.555,510.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,996.952,272.823);
   pline->SetPoint(1,1011.458,228.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1008.236,278.823);
   pline->SetPoint(1,1022.742,234.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,986.57,673.45);
   pline->SetPoint(1,1087.07,673.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,986.57,705.05);
   pline->SetPoint(1,1087.07,705.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,986.57,846.45);
   pline->SetPoint(1,1087.07,846.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,986.57,878.05);
   pline->SetPoint(1,1087.07,878.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,986.57,1069.45);
   pline->SetPoint(1,1087.07,1069.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,986.57,1101.05);
   pline->SetPoint(1,1087.07,1101.05);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1039.341,392.763);
   pline->SetPoint(1,1056.927,349.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1050.544,399.763);
   pline->SetPoint(1,1068.129,356.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1063.433,542.827);
   pline->SetPoint(1,1086.905,502.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1072.967,550.827);
   pline->SetPoint(1,1096.439,510.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1100.42,92.45);
   pline->SetPoint(1,1100.42,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1100.42,159.99);
   pline->SetPoint(1,1100.42,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1105.92,92.45);
   pline->SetPoint(1,1105.92,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1105.92,159.99);
   pline->SetPoint(1,1105.92,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1112.92,74.45);
   pline->SetPoint(1,1112.92,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1112.92,126.65);
   pline->SetPoint(1,1112.92,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1118.42,74.45);
   pline->SetPoint(1,1118.42,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1118.42,126.65);
   pline->SetPoint(1,1118.42,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1076.26,668.95);
   pline->SetPoint(1,1176.76,668.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1076.26,700.55);
   pline->SetPoint(1,1176.76,700.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1076.26,841.95);
   pline->SetPoint(1,1176.76,841.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1076.26,873.55);
   pline->SetPoint(1,1176.76,873.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1076.26,1064.95);
   pline->SetPoint(1,1176.76,1064.95);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1076.26,1096.55);
   pline->SetPoint(1,1176.76,1096.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1167.62,542.827);
   pline->SetPoint(1,1191.092,502.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1172.749,392.763);
   pline->SetPoint(1,1190.335,349.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1175.079,272.823);
   pline->SetPoint(1,1189.585,228.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1177.154,550.827);
   pline->SetPoint(1,1200.626,510.173);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1183.952,399.763);
   pline->SetPoint(1,1201.537,356.237);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1186.363,278.823);
   pline->SetPoint(1,1200.87,234.177);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.495,283.252);
   pline->SetPoint(1,1288.495,236.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.495,364.307);
   pline->SetPoint(1,1288.495,317.363);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.495,443.645);
   pline->SetPoint(1,1288.495,396.701);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.495,522.225);
   pline->SetPoint(1,1288.495,475.281);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.495,600.141);
   pline->SetPoint(1,1288.495,553.197);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.55,739.641);
   pline->SetPoint(1,1288.55,639.141);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.55,904.8);
   pline->SetPoint(1,1288.55,804.3);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1288.55,1073.41);
   pline->SetPoint(1,1288.55,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.54,739.641);
   pline->SetPoint(1,1303.54,639.141);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.54,904.8);
   pline->SetPoint(1,1303.54,804.3);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.54,1073.41);
   pline->SetPoint(1,1303.54,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.595,283.252);
   pline->SetPoint(1,1303.595,236.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.595,364.307);
   pline->SetPoint(1,1303.595,317.363);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.595,443.645);
   pline->SetPoint(1,1303.595,396.701);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.595,522.225);
   pline->SetPoint(1,1303.595,475.281);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1303.595,600.141);
   pline->SetPoint(1,1303.595,553.197);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1320.005,331);
   pline->SetPoint(1,1320.005,284.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1320.005,414);
   pline->SetPoint(1,1320.005,367.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1320.005,494.2);
   pline->SetPoint(1,1320.005,447.256);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1320.005,573.7);
   pline->SetPoint(1,1320.005,526.756);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1320.005,655.1);
   pline->SetPoint(1,1320.005,608.156);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1320.06,838);
   pline->SetPoint(1,1320.06,737.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1320.06,1013.4);
   pline->SetPoint(1,1320.06,912.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1335.05,838);
   pline->SetPoint(1,1335.05,737.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1335.05,1013.4);
   pline->SetPoint(1,1335.05,912.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1335.105,331);
   pline->SetPoint(1,1335.105,284.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1335.105,414);
   pline->SetPoint(1,1335.105,367.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1335.105,494.2);
   pline->SetPoint(1,1335.105,447.256);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1335.105,573.7);
   pline->SetPoint(1,1335.105,526.756);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1335.105,655.1);
   pline->SetPoint(1,1335.105,608.156);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1388,92.45);
   pline->SetPoint(1,1388,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1388,159.99);
   pline->SetPoint(1,1388,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1393.5,92.45);
   pline->SetPoint(1,1393.5,49);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1393.5,159.99);
   pline->SetPoint(1,1393.5,116.54);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1400.5,74.45);
   pline->SetPoint(1,1400.5,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1400.5,126.65);
   pline->SetPoint(1,1400.5,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#cc0000");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1406,74.45);
   pline->SetPoint(1,1406,31);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1406,126.65);
   pline->SetPoint(1,1406,83.2);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.695,283.252);
   pline->SetPoint(1,1526.695,236.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.695,364.307);
   pline->SetPoint(1,1526.695,317.363);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.695,443.645);
   pline->SetPoint(1,1526.695,396.701);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.695,522.225);
   pline->SetPoint(1,1526.695,475.281);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.695,600.141);
   pline->SetPoint(1,1526.695,553.197);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.75,739.641);
   pline->SetPoint(1,1526.75,639.141);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.75,904.8);
   pline->SetPoint(1,1526.75,804.3);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1526.75,1073.41);
   pline->SetPoint(1,1526.75,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.74,739.641);
   pline->SetPoint(1,1541.74,639.141);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.74,904.8);
   pline->SetPoint(1,1541.74,804.3);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.74,1073.41);
   pline->SetPoint(1,1541.74,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.795,283.252);
   pline->SetPoint(1,1541.795,236.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.795,364.307);
   pline->SetPoint(1,1541.795,317.363);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.795,443.645);
   pline->SetPoint(1,1541.795,396.701);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.795,522.225);
   pline->SetPoint(1,1541.795,475.281);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1541.795,600.141);
   pline->SetPoint(1,1541.795,553.197);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1558.205,331);
   pline->SetPoint(1,1558.205,284.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1558.205,414);
   pline->SetPoint(1,1558.205,367.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1558.205,494.2);
   pline->SetPoint(1,1558.205,447.256);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1558.205,573.7);
   pline->SetPoint(1,1558.205,526.756);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1558.205,655.1);
   pline->SetPoint(1,1558.205,608.156);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1558.26,838);
   pline->SetPoint(1,1558.26,737.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1558.26,1013.4);
   pline->SetPoint(1,1558.26,912.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1573.25,838);
   pline->SetPoint(1,1573.25,737.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1573.25,1013.4);
   pline->SetPoint(1,1573.25,912.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1573.305,331);
   pline->SetPoint(1,1573.305,284.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1573.305,414);
   pline->SetPoint(1,1573.305,367.056);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1573.305,494.2);
   pline->SetPoint(1,1573.305,447.256);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1573.305,573.7);
   pline->SetPoint(1,1573.305,526.756);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1573.305,655.1);
   pline->SetPoint(1,1573.305,608.156);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1744,106.35);
   pline->SetPoint(1,1744,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1744,181.3);
   pline->SetPoint(1,1744,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1744,253.95);
   pline->SetPoint(1,1744,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1748,144);
   pline->SetPoint(1,1748,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1748,217.9);
   pline->SetPoint(1,1748,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1752,106.35);
   pline->SetPoint(1,1752,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1752,181.3);
   pline->SetPoint(1,1752,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1752,253.95);
   pline->SetPoint(1,1752,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1756,144);
   pline->SetPoint(1,1756,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1756,217.9);
   pline->SetPoint(1,1756,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1829.05,715.153);
   pline->SetPoint(1,1829.05,614.653);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1830.095,412.101);
   pline->SetPoint(1,1830.095,365.157);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1830.095,494.631);
   pline->SetPoint(1,1830.095,447.687);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1830.095,575.153);
   pline->SetPoint(1,1830.095,528.209);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1830.15,894.812);
   pline->SetPoint(1,1830.15,794.312);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1830.15,1073.41);
   pline->SetPoint(1,1830.15,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1845.14,894.812);
   pline->SetPoint(1,1845.14,794.312);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1845.14,1073.41);
   pline->SetPoint(1,1845.14,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1845.195,412.101);
   pline->SetPoint(1,1845.195,365.157);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1845.195,494.631);
   pline->SetPoint(1,1845.195,447.687);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1845.195,575.153);
   pline->SetPoint(1,1845.195,528.209);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1846.24,715.153);
   pline->SetPoint(1,1846.24,614.653);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1861.605,378.252);
   pline->SetPoint(1,1861.605,331.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1861.605,460.726);
   pline->SetPoint(1,1861.605,413.782);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1861.605,543.593);
   pline->SetPoint(1,1861.605,496.649);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1861.605,625.9);
   pline->SetPoint(1,1861.605,578.956);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1861.66,818);
   pline->SetPoint(1,1861.66,717.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1861.66,1000.17);
   pline->SetPoint(1,1861.66,899.67);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1876.65,818);
   pline->SetPoint(1,1876.65,717.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1876.65,1000.17);
   pline->SetPoint(1,1876.65,899.67);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1876.705,378.252);
   pline->SetPoint(1,1876.705,331.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1876.705,460.726);
   pline->SetPoint(1,1876.705,413.782);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1876.705,543.593);
   pline->SetPoint(1,1876.705,496.649);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,1876.705,625.9);
   pline->SetPoint(1,1876.705,578.956);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2003.59,106.35);
   pline->SetPoint(1,2003.59,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2003.59,181.3);
   pline->SetPoint(1,2003.59,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2003.59,253.95);
   pline->SetPoint(1,2003.59,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2007.59,144);
   pline->SetPoint(1,2007.59,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2007.59,217.9);
   pline->SetPoint(1,2007.59,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2011.59,106.35);
   pline->SetPoint(1,2011.59,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2011.59,181.3);
   pline->SetPoint(1,2011.59,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2011.59,253.95);
   pline->SetPoint(1,2011.59,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2015.59,144);
   pline->SetPoint(1,2015.59,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2015.59,217.9);
   pline->SetPoint(1,2015.59,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2191.84,715.153);
   pline->SetPoint(1,2191.84,614.653);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2192.885,412.101);
   pline->SetPoint(1,2192.885,365.157);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2192.885,494.631);
   pline->SetPoint(1,2192.885,447.687);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2192.885,575.153);
   pline->SetPoint(1,2192.885,528.209);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2192.94,894.812);
   pline->SetPoint(1,2192.94,794.312);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2192.94,1073.41);
   pline->SetPoint(1,2192.94,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2207.93,894.812);
   pline->SetPoint(1,2207.93,794.312);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2207.93,1073.41);
   pline->SetPoint(1,2207.93,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2207.985,412.101);
   pline->SetPoint(1,2207.985,365.157);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2207.985,494.631);
   pline->SetPoint(1,2207.985,447.687);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2207.985,575.153);
   pline->SetPoint(1,2207.985,528.209);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2209.03,715.153);
   pline->SetPoint(1,2209.03,614.653);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2224.395,378.252);
   pline->SetPoint(1,2224.395,331.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2224.395,460.726);
   pline->SetPoint(1,2224.395,413.782);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2224.395,543.593);
   pline->SetPoint(1,2224.395,496.649);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2224.395,625.9);
   pline->SetPoint(1,2224.395,578.956);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2224.45,818);
   pline->SetPoint(1,2224.45,717.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2224.45,1000.17);
   pline->SetPoint(1,2224.45,899.67);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2239.44,818);
   pline->SetPoint(1,2239.44,717.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2239.44,1000.17);
   pline->SetPoint(1,2239.44,899.67);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2239.495,378.252);
   pline->SetPoint(1,2239.495,331.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2239.495,460.726);
   pline->SetPoint(1,2239.495,413.782);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2239.495,543.593);
   pline->SetPoint(1,2239.495,496.649);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2239.495,625.9);
   pline->SetPoint(1,2239.495,578.956);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2301.69,106.35);
   pline->SetPoint(1,2301.69,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2301.69,181.3);
   pline->SetPoint(1,2301.69,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2301.69,253.95);
   pline->SetPoint(1,2301.69,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2305.69,144);
   pline->SetPoint(1,2305.69,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2305.69,217.9);
   pline->SetPoint(1,2305.69,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2309.69,106.35);
   pline->SetPoint(1,2309.69,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2309.69,181.3);
   pline->SetPoint(1,2309.69,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2309.69,253.95);
   pline->SetPoint(1,2309.69,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2313.69,144);
   pline->SetPoint(1,2313.69,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2313.69,217.9);
   pline->SetPoint(1,2313.69,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2625.65,715.153);
   pline->SetPoint(1,2625.65,614.653);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2626.695,412.101);
   pline->SetPoint(1,2626.695,365.157);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2626.695,494.631);
   pline->SetPoint(1,2626.695,447.687);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2626.695,575.153);
   pline->SetPoint(1,2626.695,528.209);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2626.75,894.812);
   pline->SetPoint(1,2626.75,794.312);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2626.75,1073.41);
   pline->SetPoint(1,2626.75,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2641.74,894.812);
   pline->SetPoint(1,2641.74,794.312);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2641.74,1073.41);
   pline->SetPoint(1,2641.74,972.91);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2641.795,412.101);
   pline->SetPoint(1,2641.795,365.157);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2641.795,494.631);
   pline->SetPoint(1,2641.795,447.687);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2641.795,575.153);
   pline->SetPoint(1,2641.795,528.209);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2642.84,715.153);
   pline->SetPoint(1,2642.84,614.653);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#663300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2644,106.35);
   pline->SetPoint(1,2644,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2644,181.3);
   pline->SetPoint(1,2644,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2644,253.95);
   pline->SetPoint(1,2644,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2648,144);
   pline->SetPoint(1,2648,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2648,217.9);
   pline->SetPoint(1,2648,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#663300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2652,106.35);
   pline->SetPoint(1,2652,62.9);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2652,181.3);
   pline->SetPoint(1,2652,137.85);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2652,253.95);
   pline->SetPoint(1,2652,210.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2656,144);
   pline->SetPoint(1,2656,100.55);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#3366ff");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2656,217.9);
   pline->SetPoint(1,2656,174.45);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2657.16,818);
   pline->SetPoint(1,2657.16,717.5);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2658.205,378.252);
   pline->SetPoint(1,2658.205,331.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2658.205,460.726);
   pline->SetPoint(1,2658.205,413.782);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2658.205,543.593);
   pline->SetPoint(1,2658.205,496.649);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2658.205,625.9);
   pline->SetPoint(1,2658.205,578.956);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2658.26,1000.17);
   pline->SetPoint(1,2658.26,899.67);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2673.25,1000.17);
   pline->SetPoint(1,2673.25,899.67);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2673.305,378.252);
   pline->SetPoint(1,2673.305,331.308);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2673.305,460.726);
   pline->SetPoint(1,2673.305,413.782);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2673.305,543.593);
   pline->SetPoint(1,2673.305,496.649);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#003399");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2673.305,625.9);
   pline->SetPoint(1,2673.305,578.956);
   pline->Draw("");
   
   pline = new TPolyLine(2,"");
   pline->SetFillColor(19);

   ci = TColor::GetColor("#ff3300");
   pline->SetLineColor(ci);
   pline->SetLineWidth(2);
   pline->SetPoint(0,2674.35,818);
   pline->SetPoint(1,2674.35,717.5);
   pline->Draw("");
   fullLayout000->Modified();
   fullLayout000->SetSelected(fullLayout000);
}
