c-----------------------------------------------------------------------------////////////////
C     Programe for computing the density contours,
C     Used while comparing the parameter estimated by two differtent methods.
C     Input File: ASCII
C     Output File: Grads File
C     Written By; 
C               Dr. Randhir Singh
C               Space Applications Centre,SAC,ISRO
C               Ahmedabad-380015
C               E-mail: randhir@sac.isro.gov.in
c-----------------------------------------------------------------------------////////////////
        real minvalue, maxvalue, cint
        integer stat
        real, allocatable :: bins(:),nn(:,:),data(:)
        write(*,*)'minvalue  ', 'maxvalue   ',  'cint '
        read(*,*)amin,amax,cint
        write(*,*)'number of columns in the file '
        read(*,*)ncolumns
        write(*,*)'position of parameter 1  ', 'position of parameter 2'
        read(*,*)para1,para2
c-----------------------------------------------------------------------------////////////////
        npoints=(amax-amin)/cint                   !! number of points
              allocate (data(ncolumns))
                allocate(nn(npoints,npoints))
                   allocate(bins(npoints))
c-----------------------------------------------------------------------------////////////////
        do jj=1,npoints
                     bins(jj)=amin+(jj-1)*cint  ! computing the bines
         enddo
              do jj=1,npoints
                 do kk=1,npoints
                    nn(jj,kk)=0.0                ! Initialization
                   enddo
              enddo
                        icount=0.0
                        xxmean=0.0
                        yymean=0.0
c-----------------------------------------------------------------------------////////////////
          open(1,file='input.dat',status='old',iostat=stat)              
          open(10,file='OUT.GRD',access='direct',recl=4*npoints*npoints) 
           if (stat .eq. 0)then 
              do
                 read(1,*,iostat=stat)(data(ii),ii=1,ncolumns)          
                 if(stat.ne.0) exit
                     xx=data(para1)                             
                     yy=data(para2)                             
C-----------------------------------------------------------------------------////////////////
C    For Statistics Calculation
C-----------------------------------------------------------------------------////////////////
             if(xx .gt. 0 .and. yy .gt. 0)then
                xxmean=xxmean+xx
                     yymean=yymean+yy
                         icount=icount+1
             endif
c-----------------------------------------------------------------------------////////////////
              do jj=1,npoints
                   do kk=1,npoints
              if(xx .ge. bins(jj) .and. xx .lt. bins(jj+1))then
              if(yy .ge. bins(kk) .and. yy .lt. bins(kk+1))then 
                       nn(jj,kk)=nn(jj,kk)+1
                        endif
                     endif
                   enddo 
              enddo
c-----------------------------------------------------------------------------////////////////
               enddo          
                    endif     
             write(10,rec=1)nn       
c-----------------------------------------------------------------------------////////////////
             xxmean=xxmean/float(icount)
             yymean=yymean/float(icount)
                                           close (1)
c-----------------------------------------------------------------------------////////////////
c-----------------------------------------------------------------------------////////////////
                       rmsd=0.0
                          bias=0.0
                               covxxyy=0.0
                                  varxx=0.0
                                   varyy=0.0
             open(1,file='input.dat',status='old',iostat=stat)          
             if (stat .eq. 0)then 
                     do
             read(1,*,iostat=stat)(data(ii),ii=1,ncolumns)              
                 if(stat.ne.0) exit
                      xx=data(para1)                          
                           yy=data(para2)                    
              if(xx .gt. 0 .and. yy .gt. 0)then
                     bias=bias+xx-yy  
                        rmsd=rmsd+(xx-yy)**2     
                           covxxyy=covxxyy+(xx-xxmean)*(yy-yymean)
                              varxx=varxx+(xx-xxmean)*(xx-xxmean)
                                  varyy=varyy+(yy-yymean)*(yy-yymean)
             endif
             enddo
             endif
                  covxxyy=covxxyy/float(icount)
                       varxx=sqrt(varxx/float(icount))
                          varyy=sqrt(varyy/float(icount))
                            corr=covxxyy/(varxx*varyy)
                             bias=bias/float(icount)
                                 rmsd=sqrt(rmsd/float(icount))
                     write(100,*)corr,bias,rmsd
        stop
        end
c-----------------------------------------------------------------------------////////////////
