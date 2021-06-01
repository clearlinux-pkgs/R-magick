#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-magick
Version  : 2.7.2
Release  : 41
URL      : https://cran.r-project.org/src/contrib/magick_2.7.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/magick_2.7.2.tar.gz
Summary  : Advanced Graphics and Image-Processing in R
Group    : Development/Tools
License  : MIT
Requires: R-magick-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-curl
Requires: R-magrittr
Requires: R-spelling
BuildRequires : ImageMagick-dev
BuildRequires : R-Rcpp
BuildRequires : R-curl
BuildRequires : R-magrittr
BuildRequires : R-spelling
BuildRequires : buildreq-R

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
%setup -q -c -n magick
cd %{_builddir}/magick

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619999605

%install
export SOURCE_DATE_EPOCH=1619999605
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magick
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magick
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library magick
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc magick || :


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
/usr/lib64/R/library/magick/libs/magick.so
