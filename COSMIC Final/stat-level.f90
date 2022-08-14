integer (kind=4)          :: stat,icnt,ixx(201)
real(kind=8)              :: aa1,aa2,bb1,bb2,cc1,cc2,hgt
real(kind=8)              :: corr,slope,intercept,bias,rmsd,std,tpw,tdx
real(kind=8)              :: minx,meanx,maxx,miny,meany,maxy,stdx,stdy
real(kind=8)              :: lev(202)
real(kind=8)              :: var10(201,8000000),var11(201,8000000)
real(kind=8)              :: var20(201,8000000),var21(201,8000000)
real(kind=8)              :: var30(201,8000000),var31(201,8000000)
real(kind=8)              :: xx(8000000),yy(8000000),diff(8000000)

!open(1,file='Output20_Test.txt',iostat=stat)
!open(1,file='Output20_Train.txt',iostat=stat)
open(1,file='Output21_Test.txt',iostat=stat)

open(991,file='profile-evp21-test.ascii')
open(992,file='profile-tmp21-test.ascii')
open(993,file='profile-prs21-test.ascii')

do jj=1,152
  lev(jj)=00+(jj-1)*100
enddo

ixx=0
stat=0
icnt=0

if(stat ==0)then
do
read(1,*,iostat=stat)hgt,aa1,aa2,bb1,bb2,cc1,cc2
if(stat /=0)exit
      icnt=icnt+1
      do jj=1,151
             if(hgt >= lev(jj) .and. hgt < lev(jj+1))then 
             ixx(jj)=ixx(jj)+1
             var10(jj,ixx(jj))=aa1
             var11(jj,ixx(jj))=aa2
             var20(jj,ixx(jj))=bb1
             var21(jj,ixx(jj))=bb2
             var30(jj,ixx(jj))=cc1
             var31(jj,ixx(jj))=cc2
            endif
     enddo
enddo
endif
write (*,*)'--- data reading over ----'
!--------------------------------------------------------
!--------------------------------------------------------
do jj=1,3
 icnt=00
  do kk=1,151
      if(jj == 1)then
        icnt=ixx(kk)
        xx=var10(kk,:) 
        yy=var11(kk,:)
      endif

      if(jj == 2)then
        icnt=ixx(kk)
        xx=var20(kk,:) 
        yy=var21(kk,:)
      endif

      if(jj == 3)then
        icnt=ixx(kk)
        xx=var30(kk,:) 
        yy=var31(kk,:)
      endif
!---------------------------------------------------------------------
! Staticstics
!---------------------------------------------------------------------
      call fit(xx,yy,icnt,corr,slope,intercept)
           meanx=sum(xx(1:icnt))/icnt
           meany=sum(yy(1:icnt))/icnt
           minx=minval(xx(1:icnt))
           miny=minval(yy(1:icnt))
           maxx=maxval(xx(1:icnt))
           maxy=maxval(yy(1:icnt))
           stdx=sqrt(sum((xx(1:icnt)-meanx)*(xx(1:icnt)-meanx))/icnt)
           stdy=sqrt(sum((yy(1:icnt)-meany)*(yy(1:icnt)-meany))/icnt)
           diff(1:icnt)=xx(1:icnt)-yy(1:icnt)
           bias=sum(diff(1:icnt))/icnt
           rmsd=sqrt(sum(diff(1:icnt)*diff(1:icnt))/icnt)
           std=sqrt(sum((diff(1:icnt)-bias)*(diff(1:icnt)-bias))/icnt)
          if(jj==1)write(991,'(13(F15.4,1x),1x,i9)')lev(kk),minx,meanx,maxx,stdx,miny,meany,maxy,stdy,bias,rmsd,std,corr,icnt
          if(jj==2)write(992,'(13(F15.4,1x),1x,i9)')lev(kk),minx,meanx,maxx,stdx,miny,meany,maxy,stdy,bias,rmsd,std,corr,icnt
          if(jj==3)write(993,'(13(F15.4,1x),1x,i9)')lev(kk),minx,meanx,maxx,stdx,miny,meany,maxy,stdy,bias,rmsd,std,corr,icnt
   enddo !! level
enddo    !! variable
stop
end
 !-------------------------------------------------------------------------------
 !-------------------------------------------------------------------------------
 SUBROUTINE fit(x,y,n,corr,slope,intercept)
 real(kind=8) x(n),y(n)
 integer(kind=4)  n
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
