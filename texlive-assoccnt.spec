Name:		texlive-assoccnt
Version:	38497
Release:	2
Summary:	Associate counters, making them step when a master steps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/assoccnt
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assoccnt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/assoccnt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means of declaring a set of counters
to be stepped, each time some 'master' counter is stepped.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/assoccnt
%doc %{_texmfdistdir}/doc/latex/assoccnt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
