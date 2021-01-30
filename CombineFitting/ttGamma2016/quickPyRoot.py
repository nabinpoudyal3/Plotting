import ROOT
# import numpy
# import array
import sys
# ROOT.gROOT.SetBatch(True)
# ROOT.gStyle.SetOptStat(1111)
# ROOT.gStyle.SetOptFit(111)

           

# c1 = ROOT.TCanvas( 'c1', '', 800,800 )

myfile = ROOT.TFile("fitDiagnostics.datacard_ele_2016.root","read")
fit_s = myfile.Get("fit_s")

print fit_s.floatParsFinal().find("nonPromptSF").getVal()
print fit_s.floatParsFinal().find("nonPromptSF").getErrorLo()
print fit_s.floatParsFinal().find("nonPromptSF").getErrorHi()









parameterDictEle  = {"nonPromptSF":"ttgammaSFelsixteenToy"} #,"TTbarSF":"TTbarSFelsixteenToy","WGSF":"WGSFelsixteenToy","ZGSF":"ZGSFelsixteenToy","OtherSF":"OtherSFelsixteenToy", "Other_norm":"OtherNormelsixteenToy"}
tree_fit_sb = myfile.Get("tree_fit_sb")
for param in parameterDictEle.keys():
	print param
	hist = ROOT.TH1F("hist","",100,-2,2)
	tree_fit_sb.Draw("%s>>hist"%param)
	hist = ROOT.gDirectory.Get('hist')
	print "==>",hist.GetMean(), hist.GetRMS()
	hist.Fit("gaus")
	fit = hist.GetFunction("gaus")
	print "==>>>",fit.GetParameter(1),fit.GetParameter(2)
	del hist



sys.exit()

letters = dir(fit_s.floatParsFinal().find("r"))
for i in letters:
	print(i)
c1.Draw()

sys.exit()





AbstractMethod
AppendPad
Browse
CheckedHash
Class
ClassName
Class_Name
Class_Version
Clear
Clone
Compare
Copy
DeclFileLine
DeclFileName
Delete
Dictionary
DistancetoPrimitive
Draw
DrawClass
DrawClone
Dump
Error
Execute
ExecuteEvent
Fatal
FillBuffer
FindObject
GetDrawOption
GetDtorOnly
GetIconName
GetName
GetObjectInfo
GetObjectStat
GetOption
GetTitle
GetUniqueID
HandleTimer
HasInconsistentHash
Hash
ImplFileLine
ImplFileName
Info
InheritsFrom
Inspect
InvertBit
IsA
IsEqual
IsFolder
IsOnHeap
IsSortable
IsZombie
MayNotUse
Notify
Obsolete
Paint
Pop
Print
Read
RecursiveRemove
ResetBit
SaveAs
SavePrimitive
SetBit
SetDrawOption
SetDtorOnly
SetName
SetNameTitle
SetObjectStat
SetTitle
SetUniqueID
ShowMembers
Sizeof
Streamer
StreamerNVirtual
SysError
TestBit
TestBits
UseCurrentStyle
Warning
Write
__add__
__assign__
__bool__
__class__
__contains__
__delattr__
__destruct__
__dict__
__dir__
__dispatch__
__doc__
__eq__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__invert__
__le__
__lt__
__module__
__mul__
__ne__
__neg__
__new__
__pos__
__python_owns__
__radd__
__reduce__
__reduce_ex__
__repr__
__rmul__
__rsub__
__rtruediv__
__setattr__
__sizeof__
__smartptr__
__str__
__sub__
__subclasshook__
__truediv__
__weakref__
clone
conditionalCovarianceMatrix
constPars
correlation
correlationHist
correlationMatrix
covQual
covarianceMatrix
createHessePdf
defaultPrintContents
defaultPrintStream
defaultPrintStyle
edm
floatParsFinal
floatParsInit
globalCorr
isIdentical
kAddress
kArgs
kBitMask
kCanDelete
kCannotPick
kClassName
kCollectionHeader
kExtras
kHasUUID
kInconsistent
kInline
kInvalidObject
kIsOnHeap
kIsReferenced
kMustCleanup
kName
kNoContextMenu
kNotDeleted
kObjInCanvas
kOverwrite
kSingleKey
kSingleLine
kStandard
kTitle
kTreeStructure
kValue
kVerbose
kWriteDelete
kZombie
lastMinuitFit
ls
minNll
nameFieldLength
numInvalidNLL
numStatusHistory
plotOn
prefitResult
printAddress
printArgs
printClassName
printExtras
printMultiline
printName
printStream
printTitle
printTree
printValue
randomizePars
reducedCovarianceMatrix
status
statusCodeHistory
statusLabelHistory
['AbstractMethod', 'AppendPad', 'Browse', 'CheckedHash', 'Class', 'ClassName', 'Class_Name', 'Class_Version', 'Clear', 'Clone',
 'Compare', 'Copy', 'DeclFileLine', 'DeclFileName', 'Delete', 'Dictionary', 'DistancetoPrimitive', 'Draw', 'DrawClass', 
 'DrawClone', 'Dump', 'Error', 'Execute', 'ExecuteEvent', 'Fatal', 'FillBuffer', 'FindObject', 'GetDrawOption', 'GetDtorOnly', 
 'GetIconName', 'GetName', 'GetObjectInfo', 'GetObjectStat', 'GetOption', 'GetTitle', 'GetUniqueID', 'HandleTimer', 'HasInconsistentHash', 
 'Hash', 'ImplFileLine', 'ImplFileName', 'Info', 'InheritsFrom', 'Inspect', 'InvertBit', 'IsA', 'IsEqual', 'IsFolder', 'IsOnHeap', 'IsSortable', 
 'IsZombie', 'MayNotUse', 'Notify', 'Obsolete', 'Paint', 'Pop', 'Print', 'Read', 'RecursiveRemove', 'ResetBit', 'SaveAs', 'SavePrimitive', 'SetBit',
 'SetDrawOption', 'SetDtorOnly', 'SetName', 'SetNameTitle', 'SetObjectStat', 'SetTitle', 'SetUniqueID', 'ShowMembers', 'Sizeof', 'Streamer',
 'StreamerNVirtual', 'SysError', 'TestBit', 'TestBits', 'UseCurrentStyle', 'Warning', 'Write', '_RooDirItem__CheckTObjectHashConsistency',
 '_RooDirItem__appendToDir', '_RooDirItem__removeFromDir', '_RooFitResult__CheckTObjectHashConsistency', '_RooFitResult__correlation', 
 '_RooFitResult__covariance', '_RooFitResult__fillCorrMatrix', '_RooFitResult__fillLegacyCorrMatrix', '_RooFitResult__fillPrefitCorrMatrix', 
 '_RooFitResult__setConstParList', '_RooFitResult__setCovQual', '_RooFitResult__setCovarianceMatrix', '_RooFitResult__setEDM', 
 '_RooFitResult__setFinalParList', '_RooFitResult__setInitParList', '_RooFitResult__setMinNLL', '_RooFitResult__setNumInvalidNLL',
 '_RooFitResult__setStatus', '_RooFitResult__setStatusHistory', '_RooPrintable__CheckTObjectHashConsistency', 
 '_TNamed__CheckTObjectHashConsistency', '_TObject__AddToTObjectTable', '_TObject__CheckTObjectHashConsistency',
 '_TObject__DoError', '_TObject__MakeZombie', '__add__', '__assign__', '__bool__', '__class__', '__cmp__',
 '__contains__', '__cppname__', '__delattr__', '__destruct__', '__dict__', '__dispatch__', '__div__', '__doc__',
 '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
 '__module__', '__mul__', '__ne__', '__new__', '__nonzero__', '__radd__', '__rdiv__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rmul__', '__rsub__', '__scope__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
 '__weakref__', '_get_smart_ptr', 'clone', 'conditionalCovarianceMatrix', 'constPars', 'correlation', 'correlationHist',
 'correlationMatrix', 'covQual', 'covarianceMatrix', 'createHessePdf', 'defaultPrintContents', 'defaultPrintStream', 'defaultPrintStyle', 
 'edm', 'floatParsFinal', 'floatParsInit', 'globalCorr', 'isIdentical', 'kAddress', 'kArgs', 'kBitMask', 'kCanDelete', 'kCannotPick',
 'kClassName', 'kCollectionHeader', 'kExtras', 'kHasUUID', 'kInconsistent', 'kInline', 'kInvalidObject', 'kIsOnHeap', 'kIsReferenced',
 'kMustCleanup', 'kName', 'kNoContextMenu', 'kNotDeleted', 'kObjInCanvas', 'kOverwrite', 'kSingleKey', 'kSingleLine', 'kStandard', 'kTitle',
 'kTreeStructure', 'kValue', 'kVerbose', 'kWriteDelete', 'kZombie', 'lastMinuitFit', 'ls', 'minNll', 'nameFieldLength', 'numInvalidNLL',
 'numStatusHistory', 'operator delete', 'operator delete[]', 'operator new', 'operator new[]', 'plotOn', 'prefitResult', 'printAddress',
 'printArgs', 'printClassName', 'printExtras', 'printMultiline', 'printName', 'printStream', 'printTitle', 'printTree', 'printValue',
 'randomizePars', 'reducedCovarianceMatrix', 'status', 'statusCodeHistory', 'statusLabelHistory']
