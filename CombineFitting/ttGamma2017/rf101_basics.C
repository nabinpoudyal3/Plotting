//////////////////////////////////////////////////////////////////////////
//
// 'BASIC FUNCTIONALITY' RooFit tutorial macro #101
// 
// Fitting, plotting, toy data generation on one-dimensional p.d.f
//
// pdf = gauss(x,m,s) 
//
//
// 07/2008 - Wouter Verkerke 
// 
/////////////////////////////////////////////////////////////////////////

#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "TCanvas.h"
#include "RooPlot.h"
#include "TAxis.h"
using namespace RooFit ;


void rf101_basics(){
// this is the real value of Higgs mass. But we can not get it directly in the detector,
// so we make invariant mass using the decay product and name it as mass as below.
RooRealVar MH("MH","mass of the Hypothetical Boson (H-boson) in GeV",125,120,130);
	
RooRealVar mass("m","m (GeV)",100,80,200); // invariant Higgs mass
RooRealVar sigma("resolution","#sigma",10,0,20); // this is the resolution of our measurement of mass and is 10GeV.

RooFormulaVar func("R","@0/@1",RooArgList(sigma,mass)); // relative resolution as a function of mass.
func.Print("v");

TCanvas *can = new TCanvas();

//make the x-axis the "mass"
RooPlot *plot = mass.frame(); 
func.plotOn(plot);

plot->Draw();
can->Draw();

RooGaussian gauss("gauss","f(m|M_{H},#sigma)",mass,MH,sigma); // generating the gaussian distribution
gauss.Print("V");

plot = mass.frame();
gauss.plotOn(plot);

MH.setVal(120);
gauss.plotOn(plot,RooFit::LineColor(kBlue));

MH.setVal(125);
gauss.plotOn(plot,RooFit::LineColor(kRed));


MH.setVal(156);

MH.setVal(135);
gauss.plotOn(plot,RooFit::LineColor(kGreen));

plot->Draw();

can->Update();
can->Draw();

RooDataSet *data = (RooDataSet*) gauss.generate(RooArgSet(mass),500); // generating the invariant mass of Higgs using the gaussian distribution

plot = mass.frame();

data->plotOn(plot);
gauss.plotOn(plot);
gauss.paramOn(plot);

plot->Draw();
can->Update();
can->Draw();


RooDataSet mydata("dummy","My dummy dataset",RooArgSet(mass)); 
// We've made a dataset with one observable (mass)

mass.setVal(123.4);
mydata.add(RooArgSet(mass));
mass.setVal(145.2);
mydata.add(RooArgSet(mass));
mass.setVal(170.8);
mydata.add(RooArgSet(mass));

mydata.Print();

}



































