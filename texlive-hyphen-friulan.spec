# revision 26595
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-friulan
Version:	20120809
Release:	5
Summary:	Friulan hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-friulan.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Friulan in ASCII encoding. They are
supposed to comply with the common spelling of the Friulan
(Furlan) language as fixed by the Regional Law N.15/96 dated
November 6, 1996 and its following amendments.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-friulan
%_texmf_language_def_d/hyphen-friulan
%_texmf_language_lua_d/hyphen-friulan

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-friulan <<EOF
\%% from hyphen-friulan:
friulan loadhyph-fur.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-friulan
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-friulan <<EOF
\%% from hyphen-friulan:
\addlanguage{friulan}{loadhyph-fur.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-friulan
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-friulan <<EOF
-- from hyphen-friulan:
	['friulan'] = {
		loader = 'loadhyph-fur.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-fur.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120809-1
+ Revision: 813566
- Import texlive-hyphen-friulan
- Import texlive-hyphen-friulan

