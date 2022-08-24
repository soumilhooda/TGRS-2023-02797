'open plot1.ctl'
'open plot2.ctl'
'open plot3.ctl'
'set xsize 1200 1500'
'set display color white'
'c'
'set grads off'
'set grid off'
'set lat 0 44'
'set lon 45 108'
'set xlint 8'
'set ylint 4'
'set annot 1 5'
'set mpdset indres'
'set xlopts 1 3 0.09'
'set ylopts 1 3 0.09'
'set font 1'
'set mproj scaled'
*------------------------------------------------------------
* upper  Row
*------------------------------------------------------------
'set parea 2 6.5 7.4 10.4'
'set gxout grfill'
*'color  -1 1 0.05 -kind honeydew->dodgerblue->blue->green->yellow->orange->darkred->fuchsia'
'set clevs -900 0.0 0.03 0.06 0.09 0.12 0.15 0.18 0.21 0.24 0.30 0.40'
'set ccols  15 14 4 11 5 13 3 10 7 12 8 2 6'
'd var.1(t=3)'
'set strsiz 0.15 0.15'
'draw string 5.6 9.7 (a)'
*------------------------------------------------------------
* middle  Row
*------------------------------------------------------------
'set parea 2 6.5 4.1 7.1'
'set gxout grfill'
'set clevs -900 0.0 0.03 0.06 0.09 0.12 0.15 0.18 0.21 0.24 0.30 0.40'
'set ccols  15 14 4 11 5 13 3 10 7 12 8 2 6'
'd var.2(t=3)'
'set strsiz 0.15 0.15'
'draw string 5.6 6.4 (b)'
'cbarn 0.99 1 6.7 5.5'
*------------------------------------------------------------
* lower  Row
*------------------------------------------------------------
'set parea 2 6.5 0.8 3.8'
'set gxout grfill'
'set clevs -900 0.0 0.03 0.06 0.09 0.12 0.15 0.18 0.21 0.24 0.30 0.40'
'set ccols  15 14 4 11 5 13 3 10 7 12 8 2 6'
'd var.3(t=3)'
'set strsiz 0.15 0.15'
'draw string 5.6 3.1 (c)'
*------------------------------------------------------------
*---------------------
'printim dist-evp-rmsd-train20-test20-test21.png'
'gxprint dist-evp-rmsd-train20-test20-test21.eps eps'
'gxprint dist-evp-rmsd-train20-test20-test21.pdf pdf'
*'quit'
*-----------------------------------------------------------------------------------
