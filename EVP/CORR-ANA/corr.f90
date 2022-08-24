integer (kind=4)          :: stat,icnt,ixx(201),ipt(32),n
real(kind=8)              :: aa1,aa2,bb1,bb2,cc1,cc2,dummy,j1,evp,j2,j3,j4,j5,j6,j7,j8,j9,j10
real(kind=8)              :: corr,slope,intercept,bias,rmsd,std,mean,tpw,tdx
real(kind=8)              :: lev(35),meany(35),meanx(35,7),miny(35),minx(35,7),& 
                             maxy(35),maxx(35,7),stdy(35),stdx(35,7)
real(kind=8)              :: var10(32,20000000),var11(32,20000000)
real(kind=8)              :: var12(32,20000000),var13(32,20000000)
real(kind=8)              :: var14(32,20000000),var15(32,20000000)
real(kind=8)              :: var16(32,20000000),var17(32,20000000)
real(kind=8)              :: xx(20000000),yy(20000000),diff(20000000),acorr(32,7)

open(3,file='ucar-hum-evp-tmp-prs-2020-2021-india-ntopo.txt',iostat=stat)

do jj=1,17
  lev(jj)=00+(jj-1)*1000
enddo

ixx=0
stat=0
icnt=0

if(stat ==0)then
do
read(3,*,iostat=stat)j1,evp,j2,j3,j4,j5,j6,j7,j8,j9,j10
if(stat /=0)exit
      icnt=icnt+1
      do jj=1,16
             if(j5 >= lev(jj) .and. j5 < lev(jj+1))then
             ixx(jj)=ixx(jj)+1
             var10(jj,ixx(jj))=j2
             var11(jj,ixx(jj))=j4
             var12(jj,ixx(jj))=j5
             var13(jj,ixx(jj))=j6
             var14(jj,ixx(jj))=j7
             var15(jj,ixx(jj))=j8
             var16(jj,ixx(jj))=j9
             var17(jj,ixx(jj))=evp
            endif
     enddo
enddo
endif
write (*,*)'--- data reading over ----'
!--------------------------------------------------------
do kk=1,16
write(*,*)kk,ixx(kk)
enddo
!--------------------------------------------------------
do jj=1,7
 icnt=00

  do kk=1,16
      if(jj == 1)then
        icnt=ixx(kk)
       yy=var10(kk,:)
       xx=var11(kk,:)
      endif

      if(jj == 2)then
        icnt=ixx(kk)
        yy=var10(kk,:)
        xx=var12(kk,:)
      endif

      if(jj == 3)then
        icnt=ixx(kk)
        yy=var10(kk,:)
        xx=var13(kk,:)
      endif

      if(jj == 4)then
        icnt=ixx(kk)
        yy=var10(kk,:)
        xx=var14(kk,:)
      endif

      if(jj == 5)then
        icnt=ixx(kk)
        yy=var10(kk,:)
        xx=var15(kk,:)
      endif


      if(jj == 6)then
        icnt=ixx(kk)
        yy=var10(kk,:)
        xx=var16(kk,:)
      endif

      if(jj == 7)then
        icnt=ixx(kk)
        yy=var10(kk,:)
        xx=var17(kk,:)
      endif
!---------------------------------------------------------------------
! Staticstics
!---------------------------------------------------------------------
      call fit(xx,yy,icnt,corr,slope,intercept)
           meanx(kk,jj)=sum(xx(1:icnt))/icnt
           minx(kk,jj)=minval(xx(1:icnt))
           maxx(kk,jj)=maxval(xx(1:icnt))
           stdx(kk,jj)=sqrt(sum((xx(1:icnt)-meanx(kk,jj))*(xx(1:icnt)-meanx(kk,jj)))/icnt)
           meany(kk)=sum(yy(1:icnt))/icnt
           miny(kk)=minval(yy(1:icnt))
           maxy(kk)=maxval(yy(1:icnt))
           stdy(kk)=sqrt(sum((yy(1:icnt)-meany(kk))*(yy(1:icnt)-meany(kk)))/icnt)
!           mean=sum(xx(1:icnt))/icnt
!           diff(1:icnt)=xx(1:icnt)-yy(1:icnt)
!           bias=sum(diff(1:icnt))/icnt
!           rmsd=sqrt(sum(diff(1:icnt)*diff(1:icnt))/icnt)
!           std=sqrt(sum((diff(1:icnt)-bias)*(diff(1:icnt)-bias))/icnt)
           acorr(kk,jj) = corr
           ipt(kk) = icnt
!         write(*,*)jj,kk,corr
   enddo !! level
enddo    !! variable

   do kk=1,15
       write(993,'(17(F10.4,1x),1x,I10)')lev(kk),lev(kk+1),miny(kk),meany(kk),maxy(kk),stdy(kk), & 
                                                          minx(kk,1),meanx(kk,1),maxx(kk,1),stdx(kk,1), &
                                                          (acorr(kk,jj),jj=1,7),ipt(kk)
   enddo !! kk level

stop
end
 !-------------------------------------------------------------------------------
 !-------------------------------------------------------------------------------
 SUBROUTINE fit(x,y,n,corr,slope,intercept)
 integer(kind=4) :: n
 real(kind=8) x(n),y(n)
 real(kind=8) slope, intercept, corr
 real(kind=8) :: sumx,sumxx,sumy,sumyy,sumxy
 sumx=0
 sumxx=0
 sumy=0
 sumyy=0
 sumxy=0
 do jj=1,n
    sumx=sumx+x(jj)
    sumxx=sumxx+x(jj)*x(jj)
    sumy=sumy+y(jj)
    sumyy=sumyy+y(jj)*y(jj)
    sumxy=sumxy+x(jj)*y(jj)
 enddo
    slope=(N*sumxy-sumx*sumy)/(N*sumxx-sumx**2)
    intercept=(sumy*sumxx-sumx*sumxy)/(N*sumxx-sumx**2)
    corr=(sumxy-sumx*sumy/N)/(sqrt((sumxx-sumx**2/N)*(sumyy-sumy**2/N)))
    return
    end
!-------------------------------------------------------------------------------
