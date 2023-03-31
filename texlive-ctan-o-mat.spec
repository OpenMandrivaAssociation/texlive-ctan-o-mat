Name:		texlive-ctan-o-mat
Version:	51578
Release:	2
Summary:	Upload or validate a package for CTAN
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ctan-o-mat
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctan-o-mat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctan-o-mat.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This program can be used to automate the upload of a package to
CTAN. The description of the package is contained in a
configuration file. The provided information is validated in
any case. If the validation succeeds and not only the
validation is requested, then the provided archive file will be
placed in the incoming area of the CTAN for further processing
by the CTAN team. In any case any finding during the validation
is reported at the end of the processing. Note that the
validation is the default and an official submission has to be
requested by an appropriate command line option. ctan-o-mat
requires an Internet connection to the CTAN server. Even the
validation retrieves the known attributes and the basic
constraints from the server.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/scripts/ctan-o-mat
%doc %{_texmfdistdir}/doc/support/ctan-o-mat
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
