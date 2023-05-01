#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-logspline
Version  : 2.1.19
Release  : 44
URL      : https://cran.r-project.org/src/contrib/logspline_2.1.19.tar.gz
Source0  : https://cran.r-project.org/src/contrib/logspline_2.1.19.tar.gz
Summary  : Routines for Logspline Density Estimation
Group    : Development/Tools
License  : Apache-2.0
Requires: R-logspline-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
The function oldlogspline() uses the same algorithm as the logspline package
	version 1.0.x; i.e. the Kooperberg and Stone (1992) 
	algorithm (with an improved interface).  The recommended routine logspline()

%package lib
Summary: lib components for the R-logspline package.
Group: Libraries

%description lib
lib components for the R-logspline package.


%prep
%setup -q -n logspline
cd %{_builddir}/logspline

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1669223612

%install
export SOURCE_DATE_EPOCH=1669223612
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/logspline/DESCRIPTION
/usr/lib64/R/library/logspline/INDEX
/usr/lib64/R/library/logspline/Meta/Rd.rds
/usr/lib64/R/library/logspline/Meta/features.rds
/usr/lib64/R/library/logspline/Meta/hsearch.rds
/usr/lib64/R/library/logspline/Meta/links.rds
/usr/lib64/R/library/logspline/Meta/nsInfo.rds
/usr/lib64/R/library/logspline/Meta/package.rds
/usr/lib64/R/library/logspline/NAMESPACE
/usr/lib64/R/library/logspline/R/logspline
/usr/lib64/R/library/logspline/R/logspline.rdb
/usr/lib64/R/library/logspline/R/logspline.rdx
/usr/lib64/R/library/logspline/help/AnIndex
/usr/lib64/R/library/logspline/help/aliases.rds
/usr/lib64/R/library/logspline/help/logspline.rdb
/usr/lib64/R/library/logspline/help/logspline.rdx
/usr/lib64/R/library/logspline/help/paths.rds
/usr/lib64/R/library/logspline/html/00Index.html
/usr/lib64/R/library/logspline/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/logspline/libs/logspline.so
/usr/lib64/R/library/logspline/libs/logspline.so.avx2
/usr/lib64/R/library/logspline/libs/logspline.so.avx512
