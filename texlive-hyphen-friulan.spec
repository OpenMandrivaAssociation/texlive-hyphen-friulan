%global tl_name hyphen-friulan
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Friulan hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-friulan
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-friulan.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Friulan in ASCII encoding. They are supposed to
comply with the common spelling of the Friulan (Furlan) language as
fixed by the Regional Law N.15/96 dated November 6, 1996 and its
following amendments.

