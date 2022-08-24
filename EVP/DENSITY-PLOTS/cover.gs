'open plot.ctl'
*'set xsize 1300 1300'
'set display color white'
'c'
'set mproj off'
'set grads off'
'set grid off'
'set lat 0 33'
'set lon 0 33'
'set xlint 3'
'set ylint 3'
'set annot 1 6'
'set xlopts 1 5 0.15'
'set ylopts 1 5 0.15'
'set font 2'
'set mproj off'
*------------------------------------------------------------
* upper  Row
*------------------------------------------------------------
'set parea 1 7.5 2 8.5'
'set gxout shaded'
'color  500 30500 500 -kind white->blue->green->yellow->orange->darkred->fuchsia'
'color  200 30200 200 -kind white->blue->green->yellow->orange->darkred->fuchsia'
*'set clevs 10 100 500 1000 5000 10000 15000 20000 25000 30000 35000'
*'set ccols 0 14 4 11 5 13 3 10 7 12 8 2 6'
'd var(t=1)'
'set line 1 1 6'
'draw line 1 2 7.5 8.5'
'draw ylab Retrieved Water Vapour Pressure(hPa)'
'draw xlab Actual Water Vapour Pressure(hPa)'
'set strsiz 0.16 0.16'
'draw string 1.1 8.29  Bias      =0.033 hPa'
'draw string 1.1 8.05  Rmsd     =0.196 hPa'
'draw string 1.1 7.80  Std.Dev   =0.194 hPa'
'draw string 1.1 7.55  %Error    =5.591     '
'draw string 1.1 7.30  count=9152900       '
*'cbarn 0.99 1 7.6 5.2'
'xcbar 7.55 7.70 2 8.5 -fskip 10'
*------------------------------------------------------------
*---------------------
'printim cover.png'
'gxprint cover.eps eps'
'gxprint cover.pdf pdf'
*'quit'
*-----------------------------------------------------------------------------------