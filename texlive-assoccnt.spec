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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means of declaring a set of counters to be
stepped, each time some 'master' counter is stepped.

