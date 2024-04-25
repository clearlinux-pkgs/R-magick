#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: da8b975
#
Name     : R-magick
Version  : 2.8.3
Release  : 64
URL      : https://cran.r-project.org/src/contrib/magick_2.8.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/magick_2.8.3.tar.gz
Summary  : Advanced Graphics and Image-Processing in R
Group    : Development/Tools
License  : MIT
Requires: R-magick-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-curl
Requires: R-magrittr
BuildRequires : ImageMagick-dev
BuildRequires : R-Rcpp
BuildRequires : R-curl
BuildRequires : R-magrittr
BuildRequires : R-spelling
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
processing library available. Supports many common formats (png, jpeg, tiff,
    pdf, etc) and manipulations (rotate, scale, crop, trim, flip, blur, etc).
    All operations are vectorized via the Magick++ STL meaning they operate either
    on a single frame or a series of frames for working with layers, collages,
    or animation. In RStudio images are automatically previewed when printed to
    the console, resulting in an interactive editing environment. The latest 
    version of the package includes a native graphics device for creating 
    in-memory graphics or drawing onto images using pixel coordinates.

%package lib
Summary: lib components for the R-magick package.
Group: Libraries

%description lib
lib components for the R-magick package.


%prep
%setup -q -n magick
pushd ..
cp -a magick buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708277273

%install
export SOURCE_DATE_EPOCH=1708277273
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/magick/DESCRIPTION
/usr/lib64/R/library/magick/INDEX
/usr/lib64/R/library/magick/LICENSE
/usr/lib64/R/library/magick/Meta/Rd.rds
/usr/lib64/R/library/magick/Meta/features.rds
/usr/lib64/R/library/magick/Meta/hsearch.rds
/usr/lib64/R/library/magick/Meta/links.rds
/usr/lib64/R/library/magick/Meta/nsInfo.rds
/usr/lib64/R/library/magick/Meta/package.rds
/usr/lib64/R/library/magick/Meta/vignette.rds
/usr/lib64/R/library/magick/NAMESPACE
/usr/lib64/R/library/magick/NEWS
/usr/lib64/R/library/magick/R/magick
/usr/lib64/R/library/magick/R/magick.rdb
/usr/lib64/R/library/magick/R/magick.rdx
/usr/lib64/R/library/magick/R/sysdata.rdb
/usr/lib64/R/library/magick/R/sysdata.rdx
/usr/lib64/R/library/magick/WORDLIST
/usr/lib64/R/library/magick/doc/index.html
/usr/lib64/R/library/magick/doc/intro.R
/usr/lib64/R/library/magick/doc/intro.Rmd
/usr/lib64/R/library/magick/doc/intro.html
/usr/lib64/R/library/magick/help/AnIndex
/usr/lib64/R/library/magick/help/aliases.rds
/usr/lib64/R/library/magick/help/magick.rdb
/usr/lib64/R/library/magick/help/magick.rdx
/usr/lib64/R/library/magick/help/paths.rds
/usr/lib64/R/library/magick/html/00Index.html
/usr/lib64/R/library/magick/html/R.css
/usr/lib64/R/library/magick/images/building.jpg
/usr/lib64/R/library/magick/images/man.gif
/usr/lib64/R/library/magick/images/objects.gif
/usr/lib64/R/library/magick/images/shape_rectangle.gif
/usr/lib64/R/library/magick/images/test_mag.gif
/usr/lib64/R/library/magick/tests/encoding.R
/usr/lib64/R/library/magick/tests/imagemagick.R
/usr/lib64/R/library/magick/tests/imagemagick.Rout.save
/usr/lib64/R/library/magick/tests/spelling.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/magick/libs/magick.so
/usr/lib64/R/library/magick/libs/magick.so
