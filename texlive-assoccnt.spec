%global tl_name assoccnt
%global tl_revision 38497

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8
Release:	%{tl_revision}.1
Summary:	Associate counters, making them step when a master steps
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/assoccnt
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/assoccnt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/assoccnt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means of declaring a set of counters to be
stepped, each time some 'master' counter is stepped.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/assoccnt
%dir %{_datadir}/texmf-dist/tex/latex/assoccnt
%doc %{_datadir}/texmf-dist/doc/latex/assoccnt/README
%doc %{_datadir}/texmf-dist/doc/latex/assoccnt/assoccnt_doc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/assoccnt/assoccnt_doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/assoccnt/assoccnt_example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/assoccnt/assoccnt_example.tex
%{_datadir}/texmf-dist/tex/latex/assoccnt/assoccnt.sty
