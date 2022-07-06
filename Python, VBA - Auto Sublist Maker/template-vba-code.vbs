
'
' Demo Close
'

Private Sub CommandButton1_Click()
    Worksheets("Combined").Rows("3").ShowDetail = False
    CommandButton1.Visible = False
    CommandButton2.Visible = True
End Sub

'
' Demo Open
'
Private Sub CommandButton2_Click()
    Worksheets("Combined").Rows("3").ShowDetail = True
    CommandButton1.Visible = True
    CommandButton2.Visible = False
End Sub


'
' Demo Refresh
'
Private Sub CommandButton3_Click()
    RefreshDemoCombined
End Sub

'
' Shoring Close
'
Private Sub CommandButton4_Click()
    Worksheets("Combined").Rows("52").ShowDetail = False
    CommandButton4.Visible = False
    CommandButton5.Visible = True
End Sub

'
' Shoring Open
'
Private Sub CommandButton5_Click()
    Worksheets("Combined").Rows("52").ShowDetail = True
    CommandButton4.Visible = True
    CommandButton5.Visible = False
End Sub

'
' Fencing Open
'
Private Sub CommandButton7_Click()
    Worksheets("Combined").Rows("102").ShowDetail = True
    CommandButton8.Visible = True
    CommandButton7.Visible = False
End Sub

'
' Refresh Shoring
'
Private Sub CommandButton6_Click()
    RefreshElectricalCombined
End Sub

'
' Fencing Close
'
Private Sub CommandButton8_Click()
    Worksheets("Combined").Rows("102").ShowDetail = False
    CommandButton8.Visible = False
    CommandButton7.Visible = True
End Sub

'
' Fencing Refresh
'
Private Sub CommandButton9_Click()
    RefreshBarriersCombined
End Sub




'
' Mechanical Close
'

Private Sub CommandButton10_click()
    Worksheets("Combined").Rows("152").ShowDetail = False
    CommandButton10.Visible = False
    CommandButton11.Visible = True
End Sub

'
' Mechanical Open
'
Private Sub CommandButton11_click()
    Worksheets("Combined").Rows("152").ShowDetail = True
    CommandButton10.Visible = True
    CommandButton11.Visible = False
End Sub

'
' Mechanical Refresh
'
Private Sub CommandButton12_click()
    RefreshFencingCombined
End Sub




'
' Rebar Refresh
'
Private Sub CommandButton13_Click()
    RefreshLandscapingCombined
End Sub

'
' Rebar Open
'
Private Sub CommandButton14_click()
    Worksheets("Combined").Rows("202").ShowDetail = True
    CommandButton15.Visible = True
    CommandButton14.Visible = False
End Sub

'
' Rebar Close
'
Private Sub CommandButton15_click()
    Worksheets("Combined").Rows("202").ShowDetail = False
    CommandButton14.Visible = True
    CommandButton15.Visible = False
End Sub




'
'Steel Close
'
Private Sub CommandButton17_click()
    Worksheets("Combined").Rows("254").ShowDetail = False
    CommandButton17.Visible = False
    CommandButton18.Visible = True
End Sub
'
'Steel Open
'
Private Sub CommandButton18_click()
    Worksheets("Combined").Rows("254").ShowDetail = True
    CommandButton17.Visible = True
    CommandButton18.Visible = False
End Sub

'
'Steel Refresh
'
Private Sub CommandButton16_click()
    RefreshSteel
End Sub




'
'Barriers Close
'
Private Sub CommandButton20_click()
    Worksheets("Combined").Rows("306").ShowDetail = False
    CommandButton20.Visible = False
    CommandButton21.Visible = True
End Sub
'
'Barriers Open
'
Private Sub CommandButton21_click()
    Worksheets("Combined").Rows("306").ShowDetail = True
    CommandButton20.Visible = True
    CommandButton21.Visible = False
End Sub

'
'Barriers Refresh
'
Private Sub CommandButton19_click()
    RefreshBarriers2
End Sub




'
'Electrical Close
'
Private Sub CommandButton23_click()
    Worksheets("Combined").Rows("358").ShowDetail = False
    CommandButton23.Visible = False
    CommandButton24.Visible = True
End Sub
'
'Electrical Open
'
Private Sub CommandButton24_click()
    Worksheets("Combined").Rows("358").ShowDetail = True
    CommandButton23.Visible = True
    CommandButton24.Visible = False
End Sub

'
'Electrical Refresh
'
Private Sub CommandButton22_click()
    RefreshElectrical2
End Sub




'
'Formwork Close
'
Private Sub CommandButton26_click()
    Worksheets("Combined").Rows("410").ShowDetail = False
    CommandButton26.Visible = False
    CommandButton27.Visible = True
End Sub
'
'Formwork Open
'
Private Sub CommandButton27_click()
    Worksheets("Combined").Rows("410").ShowDetail = True
    CommandButton26.Visible = True
    CommandButton27.Visible = False
End Sub

'
'Formwork Refresh
'
Private Sub CommandButton25_click()
    RefreshFormwork
End Sub




'
'Auto Doors Close
'
Private Sub CommandButton29_click()
    Worksheets("Combined").Rows("462").ShowDetail = False
    CommandButton29.Visible = False
    CommandButton30.Visible = True
End Sub
'
'Auto Doors Open
'
Private Sub CommandButton30_click()
    Worksheets("Combined").Rows("462").ShowDetail = True
    CommandButton29.Visible = True
    CommandButton30.Visible = False
End Sub

'
'Auto Doors Refresh
'
Private Sub CommandButton28_click()
    RefreshAutodoors
End Sub




'
'Caulking Close
'
Private Sub CommandButton32_click()
    Worksheets("Combined").Rows("514").ShowDetail = False
    CommandButton32.Visible = False
    CommandButton33.Visible = True
End Sub
'
'Caulking Open
'
Private Sub CommandButton33_click()
    Worksheets("Combined").Rows("514").ShowDetail = True
    CommandButton32.Visible = True
    CommandButton33.Visible = False
End Sub

'
'Caulking Refresh
'
Private Sub CommandButton31_click()
    RefreshCaulking
End Sub




'
'Communication Close
'
Private Sub CommandButton35_click()
    Worksheets("Combined").Rows("566").ShowDetail = False
    CommandButton35.Visible = False
    CommandButton36.Visible = True
End Sub
'
'Communication Open
'
Private Sub CommandButton36_click()
    Worksheets("Combined").Rows("566").ShowDetail = True
    CommandButton35.Visible = True
    CommandButton36.Visible = False
End Sub

'
'Communication Refresh
'
Private Sub CommandButton34_click()
    RefreshCommunication
End Sub




'
'Doors Close
'
Private Sub CommandButton38_click()
    Worksheets("Combined").Rows("618").ShowDetail = False
    CommandButton38.Visible = False
    CommandButton39.Visible = True
End Sub
'
'Doors Open
'
Private Sub CommandButton39_click()
    Worksheets("Combined").Rows("618").ShowDetail = True
    CommandButton38.Visible = True
    CommandButton39.Visible = False
End Sub

'
'Doors Refresh
'
Private Sub CommandButton37_click()
    RefreshDoors
End Sub



'
'Drywall Close
'
Private Sub CommandButton41_click()
    Worksheets("Combined").Rows("670").ShowDetail = False
    CommandButton41.Visible = False
    CommandButton42.Visible = True
End Sub
'
'Drywall Open
'
Private Sub CommandButton42_click()
    Worksheets("Combined").Rows("670").ShowDetail = True
    CommandButton41.Visible = True
    CommandButton42.Visible = False
End Sub

'
'Drywall Refresh
'
Private Sub CommandButton40_click()
    RefreshDrywall
End Sub



'
'Elevator Close
'
Private Sub CommandButton44_click()
    Worksheets("Combined").Rows("722").ShowDetail = False
    CommandButton44.Visible = False
    CommandButton45.Visible = True
End Sub
'
'Elevator Open
'
Private Sub CommandButton45_click()
    Worksheets("Combined").Rows("722").ShowDetail = True
    CommandButton44.Visible = True
    CommandButton45.Visible = False
End Sub

'
'Elevator Refresh
'
Private Sub CommandButton43_click()
    RefreshElevator
End Sub



'
'Fall Close
'
Private Sub CommandButton47_click()
    Worksheets("Combined").Rows("774").ShowDetail = False
    CommandButton47.Visible = False
    CommandButton48.Visible = True
End Sub
'
'Fall Open
'
Private Sub CommandButton48_click()
    Worksheets("Combined").Rows("774").ShowDetail = True
    CommandButton47.Visible = True
    CommandButton48.Visible = False
End Sub

'
'Fall Refresh
'
Private Sub CommandButton46_click()
    RefreshFall
End Sub



'
'Fire Close
'
Private Sub CommandButton50_click()
    Worksheets("Combined").Rows("826").ShowDetail = False
    CommandButton50.Visible = False
    CommandButton51.Visible = True
End Sub
'
'Fire Open
'
Private Sub CommandButton51_click()
    Worksheets("Combined").Rows("826").ShowDetail = True
    CommandButton50.Visible = True
    CommandButton51.Visible = False
End Sub

'
'Fire Refresh
'
Private Sub CommandButton49_click()
    RefreshFire
End Sub



'
'Landscaping Close
'
Private Sub CommandButton56_click()
    Worksheets("Combined").Rows("930").ShowDetail = False
    CommandButton56.Visible = False
    CommandButton57.Visible = True
End Sub
'
'Landscaping Open
'
Private Sub CommandButton57_click()
    Worksheets("Combined").Rows("930").ShowDetail = True
    CommandButton56.Visible = True
    CommandButton57.Visible = False
End Sub

'
'Landscaping Refresh
'
Private Sub CommandButton55_click()
    RefreshLandscaping
End Sub



'
'Flooring Close
'
Private Sub CommandButton53_click()
    Worksheets("Combined").Rows("878").ShowDetail = False
    CommandButton53.Visible = False
    CommandButton54.Visible = True
End Sub
'
'Flooring Open
'
Private Sub CommandButton54_click()
    Worksheets("Combined").Rows("878").ShowDetail = True
    CommandButton53.Visible = True
    CommandButton54.Visible = False
End Sub

'
'Flooring Refresh
'
Private Sub CommandButton52_click()
    RefreshFlooring
End Sub



'
'Louvers Close
'
Private Sub CommandButton59_click()
    Worksheets("Combined").Rows("982").ShowDetail = False
    CommandButton59.Visible = False
    CommandButton60.Visible = True
End Sub
'
'Louvers Open
'
Private Sub CommandButton60_click()
    Worksheets("Combined").Rows("982").ShowDetail = True
    CommandButton59.Visible = True
    CommandButton60.Visible = False
End Sub

'
'Louvers Refresh
'
Private Sub CommandButton58_click()
    RefreshLouvers
End Sub



'
'Masonry Close
'
Private Sub CommandButton62_click()
    Worksheets("Combined").Rows("1034").ShowDetail = False
    CommandButton62.Visible = False
    CommandButton63.Visible = True
End Sub
'
'Masonry Open
'
Private Sub CommandButton63_click()
    Worksheets("Combined").Rows("1034").ShowDetail = True
    CommandButton62.Visible = True
    CommandButton63.Visible = False
End Sub

'
'Masonry Refresh
'
Private Sub CommandButton61_click()
    RefreshMasonry
End Sub



'
'Siding Close
'
Private Sub CommandButton65_click()
    Worksheets("Combined").Rows("1086").ShowDetail = False
    CommandButton65.Visible = False
    CommandButton66.Visible = True
End Sub
'
'Siding Open
'
Private Sub CommandButton66_click()
    Worksheets("Combined").Rows("1086").ShowDetail = True
    CommandButton65.Visible = True
    CommandButton66.Visible = False
End Sub

'
'Siding Refresh
'
Private Sub CommandButton64_click()
    RefreshSiding
End Sub



'
'Monitoring Close
'
Private Sub CommandButton68_click()
    Worksheets("Combined").Rows("1138").ShowDetail = False
    CommandButton68.Visible = False
    CommandButton69.Visible = True
End Sub
'
'Monitoring Open
'
Private Sub CommandButton69_click()
    Worksheets("Combined").Rows("1138").ShowDetail = True
    CommandButton68.Visible = True
    CommandButton69.Visible = False
End Sub

'
'Monitoring Refresh
'
Private Sub CommandButton67_click()
    RefreshMonitoring
End Sub



'
'Painting Close
'
Private Sub CommandButton71_click()
    Worksheets("Combined").Rows("1190").ShowDetail = False
    CommandButton71.Visible = False
    CommandButton72.Visible = True
End Sub
'
'Painting Open
'
Private Sub CommandButton72_click()
    Worksheets("Combined").Rows("1190").ShowDetail = True
    CommandButton71.Visible = True
    CommandButton72.Visible = False
End Sub

'
'Painting Refresh
'
Private Sub CommandButton70_click()
    RefreshPainting
End Sub



'
'Railing Close
'
Private Sub CommandButton74_click()
    Worksheets("Combined").Rows("1242").ShowDetail = False
    CommandButton74.Visible = False
    CommandButton75.Visible = True
End Sub
'
'Railing Open
'
Private Sub CommandButton75_click()
    Worksheets("Combined").Rows("1242").ShowDetail = True
    CommandButton74.Visible = True
    CommandButton75.Visible = False
End Sub

'
'Railing Refresh
'
Private Sub CommandButton73_click()
    RefreshRailing
End Sub



'
'Roofing Close
'
Private Sub CommandButton77_click()
    Worksheets("Combined").Rows("1294").ShowDetail = False
    CommandButton77.Visible = False
    CommandButton78.Visible = True
End Sub
'
'Roofing Open
'
Private Sub CommandButton78_click()
    Worksheets("Combined").Rows("1294").ShowDetail = True
    CommandButton77.Visible = True
    CommandButton78.Visible = False
End Sub

'
'Roofing Refresh
'
Private Sub CommandButton76_click()
    RefreshRoofing
End Sub



'
'Signs Close
'
Private Sub CommandButton80_click()
    Worksheets("Combined").Rows("1346").ShowDetail = False
    CommandButton80.Visible = False
    CommandButton81.Visible = True
End Sub
'
'Signs Open
'
Private Sub CommandButton81_click()
    Worksheets("Combined").Rows("1346").ShowDetail = True
    CommandButton80.Visible = True
    CommandButton81.Visible = False
End Sub

'
'Signs Refresh
'
Private Sub CommandButton79_click()
    RefreshSigns
End Sub



'
'Tree Cutting Close
'
Private Sub CommandButton83_click()
    Worksheets("Combined").Rows("1398").ShowDetail = False
    CommandButton83.Visible = False
    CommandButton84.Visible = True
End Sub
'
'Tree Cutting Open
'
Private Sub CommandButton84_click()
    Worksheets("Combined").Rows("1398").ShowDetail = True
    CommandButton83.Visible = True
    CommandButton84.Visible = False
End Sub

'
'Tree Cutting Refresh
'
Private Sub CommandButton82_click()
    RefreshTree
End Sub



'
'Watermain Close
'
Private Sub CommandButton86_click()
    Worksheets("Combined").Rows("1450").ShowDetail = False
    CommandButton86.Visible = False
    CommandButton87.Visible = True
End Sub
'
'Watermain Open
'
Private Sub CommandButton87_click()
    Worksheets("Combined").Rows("1450").ShowDetail = True
    CommandButton86.Visible = True
    CommandButton87.Visible = False
End Sub

'
'Watermain Refresh
'
Private Sub CommandButton85_click()
    RefreshWatermain
End Sub



'
'Windows Close
'
Private Sub CommandButton89_click()
    Worksheets("Combined").Rows("1502").ShowDetail = False
    CommandButton89.Visible = False
    CommandButton90.Visible = True
End Sub
'
'Windows Open
'
Private Sub CommandButton90_click()
    Worksheets("Combined").Rows("1502").ShowDetail = True
    CommandButton89.Visible = True
    CommandButton90.Visible = False
End Sub

'
'Windows Refresh
'
Private Sub CommandButton88_click()
    RefreshWindows
End Sub
