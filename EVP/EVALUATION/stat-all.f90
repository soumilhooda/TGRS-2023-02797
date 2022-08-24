integer (kind=4)          :: stat,icnt
real(kind=8)              :: aa1,aa2,bb1,bb2,cc1,cc2,dummy,alat,alon,hgt,mon
real(kind=8)              :: corr,slope,intercept,bias,rmsd,std,mean,tpw,tdx
real(kind=8),allocatable  :: hum1(:),hum2(:),tmp1(:),tmp2(:),prs1(:),prs2(:)
real(kind=8),allocatable  :: xx(:),yy(:),diff(:)
!open(1,file='Output20_Train.txt',iostat=stat)
!open(1,file='Output20.txt',iostat=stat)
open(1,file='Output21.txt',iostat=stat)

stat=0
icnt=0
if(stat ==0)then
do
read(1,*,iostat=stat)dummy
if(stat /=0)exit
icnt=icnt+1
enddo
endif

write(*,*)icnt
rewind (1)

allocate(hum1(icnt),tmp1(icnt),prs1(icnt))
allocate(hum2(icnt),tmp2(icnt),prs2(icnt))
allocate(xx(icnt),yy(icnt),diff(icnt))

icnt=0
stat=0
if(stat ==0)then
do
read(1,*,iostat=stat)alat,alon,hgt,aa1,aa2,mon
if(stat /=0)exit
 icnt=icnt+1
    hum1(icnt)=34.6566*aa1
    hum2(icnt)=34.6566*aa2
!    tmp1(icnt)=bb1
!    tmp2(icnt)=bb2
!    prs1(icnt)=cc1
!    prs2(icnt)=cc2
enddo
endif

do jj=1,1 !3
   if(jj==1)then
    xx=hum1
    yy=hum2
   endif
   if(jj==2)then
    xx=tmp1
    yy=tmp2
   endif
   if(jj==3)then
    xx=prs1
    yy=prs2
   endif
!---------------------------------------------------------------------
!---------------------------------------------------------------------
! Staticstics
!---------------------------------------------------------------------
      call fit(xx,yy,icnt,corr,slope,intercept)
           mean=sum(xx(1:icnt))/icnt
           diff(1:icnt)=xx(1:icnt)-yy(1:icnt)
           bias=sum(diff(1:icnt))/icnt
           rmsd=sqrt(sum(diff(1:icnt)*diff(1:icnt))/icnt)
           std=sqrt(sum((diff(1:icnt)-bias)*(diff(1:icnt)-bias))/icnt)
          write(*,'(18(F9.4,1x))')mean,bias,rmsd,std,100*std/mean,corr,slope
enddo
stop
end
 !-------------------------------------------------------------------------------
 !-------------------------------------------------------------------------------
 SUBROUTINE fit(x,y,n,corr,slope,intercept)
 real(kind=8) x(n),y(n)
 real(kind=8) slope, intercept, corr
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
