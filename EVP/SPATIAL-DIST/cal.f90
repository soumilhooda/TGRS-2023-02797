integer                :: stat,jj,kk,ll,nx,ny, inx,inbox,in,inn,jn,jnn,icnt,ip
Real                   :: alatmin,alatmax,alonmin,alonmax,gridreso,ixx,iyy,val
real                   :: aa1,aa2,bb1,bb2,cc1,cc2,hgt,alat,alon,mon
real                   :: hum1(33,23,1000000),hum2(33,23,1000000)
!real                  :: tmp1(33,23,40000),tmp2(33,23,40000)
!real                  :: prs1(33,23,40000),prs2(33,23,40000)
real                   :: blat(60),blon(60), points(33,23)
real                   :: xx(1000000),yy(1000000),diff(1000000)
real                   :: corr,slope,intercept,bias,rmsd,std,mean,tpw,tdx
real                   :: amean(33,23),abias(33,23),armsd(33,23),astd(33,23),acnt(33,23)
parameter(alatmin=0,alatmax=44,alonmin=45,alonmax=110,gridreso=2)
!-----------------------------------------------
open(1,file='Output20_Train.txt',iostat=stat)
open(999,file='err2020-train.grd',access='direct',recl=4*33*23)
!-----------------------------------------------
nx=(alonmax-alonmin)/gridreso+1
ny=(alatmax-alatmin)/gridreso+1
write(*,*)nx,ny

do jj=1,nx
  blon(jj)=alonmin+(jj-1)*gridreso
enddo

do jj=1,ny
   blat(jj)=alatmin+(jj-1)*gridreso
enddo
!-----------------------------------------------
!-----------------------------------------------
points=0
if(stat ==0)then
do
read(1,*,iostat=stat)alat,alon,hgt,aa1,aa2,mon
if(stat /=0)exit
   ixx=(alon-alonmin)/gridreso+1.0                            !!! X Postion of grid point
   iyy=(alat-alatmin)/gridreso+1.0                            !!! Y position of grid point
    in=floor(ixx)
    inn=ceiling(ixx)
    jn=floor(iyy)
    jnn=ceiling(iyy)
    inx = inbox(alon, alat, blon(in),blon(inn),blat(jn),blat(jnn))
         if(inx .eq.1 .and. hgt >= 000 .and. hgt <= 15000) then
             points(in,jn)=points(in,jn)+1
             ip=points(in,jn)
             hum1(in,jn,ip)=34.6566*aa1
             hum2(in,jn,ip)=34.6566*aa2
!             tmp1(in,jn,ip)=bb1
!             tmp2(in,jn,ip)=bb2
!             prs1(in,jn,ip)=cc1
!             prs2(in,jn,ip)=cc2
         endif
enddo        !! number of Flie
endif        !! Number of File
write(*,*)'reading over'
!--------------------------------------------------------------------
!--------------------------------------------------------------------
amean=-999.0
abias=-999.0
armsd=-999
astd=-999
acnt=-999
do jj=1,nx
  do kk=1,ny
          icnt=points(jj,kk)
          if(icnt== 0)icnt=1
          xx(1:icnt)=hum1(jj,kk,1:icnt)
          yy(1:icnt)=hum2(jj,kk,1:icnt)

           call fit(xx,yy,icnt,corr,slope,intercept)
           mean=sum(xx(1:icnt))/icnt
           diff(1:icnt)=xx(1:icnt)-yy(1:icnt)
           bias=sum(diff(1:icnt))/icnt
           rmsd=sqrt(sum(diff(1:icnt)*diff(1:icnt))/icnt)
           std=sqrt(sum((diff(1:icnt)-bias)*(diff(1:icnt)-bias))/icnt)
           if(icnt > 1)write(888,'(7(F9.4,1x),2x,I6)')blat(kk),blon(jj),mean,bias,rmsd,std,corr,icnt
if(icnt >=500)then
   amean(jj,kk)=mean
   abias(jj,kk)=bias
   armsd(jj,kk)=rmsd
   astd(jj,kk)=std
   acnt(jj,kk)=icnt
 endif

enddo
enddo
write(999,rec=1)amean
write(999,rec=2)abias
write(999,rec=3)armsd
write(999,rec=4)astd
write(999,rec=5)acnt
!-----------------------------------------------------------------------
stop
end
!-----------------------------------------------------------------------
!   Inbox Function
!-----------------------------------------------------------------------
integer function inbox(x,y,xl,xr,yb,yt)
implicit none
real x, y, xl, xr, yb, yt
if(x.gt.xl.and.x.lt.xr.and.y.gt.yb.and.y.lt.yt) then
   inbox=1
else
  inbox=0
endif
return
end function inbox
!-----------------------------------------------------------------------
!-----------------------------------------------------------------------
 SUBROUTINE fit(x,y,n,corr,slope,intercept)
 real x(n),y(n)
 real slope, intercept, corr
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
!-----------------------------------------------------------------------
!-----------------------------------------------------------------------
