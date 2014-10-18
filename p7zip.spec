Summary:	Command-line version of the 7zip compressed file archiver
Name:		p7zip
Version:	9.20.1
Release:	2
License:	LGPL v2.1+
Group:		Applications/Archiving
Source0:	http://downloads.sourceforge.net/p7zip/%{name}_%{version}_src_all.tar.bz2
# Source0-md5:	bd6caaea567dc0d995c990c5cc883c89
URL:		http://p7zip.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command-line version of the 7zip compressed file archiver.

%package standalone
Summary:	Standalone 7zip executable
Group:		Applications/Archiving

%description standalone
Standalone version of 7zip. It handles less archive formats than
plugin capable version.

%prep
%setup -qn %{name}_%{version}

%{__sed} -i -e 's/ -s / /' makefile.machine

find . -name '*.cpp' -exec sed -i -e 's@getenv("P7ZIP_HOME_DIR")@"%{_libdir}/%{name}/"@g' {} \;

%build
%{__make} all2 \
	CC="%{__cc} \$(ALLFLAGS)"	\
	CXX="%{__cxx} \$(ALLFLAGS)"	\
	LDFLAGS="%{rpmldflags}"		\
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}/{Codecs,Formats},%{_mandir}/man1}

install bin/{7z,7za} $RPM_BUILD_ROOT%{_bindir}
install bin/7z.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install bin/Codecs/* $RPM_BUILD_ROOT%{_libdir}/%{name}/Codecs
install bin/7zCon.sfx $RPM_BUILD_ROOT%{_libdir}/%{name}

install man1/7z* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOCS/{MANUAL,{7zFormat,License,Methods,history,lzma,readme}.txt} ChangeLog README TODO
%attr(755,root,root) %{_bindir}/7z
%attr(755,root,root) %{_libdir}/%{name}/7z.so
%attr(755,root,root) %{_libdir}/%{name}/7zCon.sfx
%attr(755,root,root) %{_libdir}/%{name}/Codecs/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/Codecs
%{_mandir}/man1/7z.1*

%files standalone
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/7za
%{_mandir}/man1/7za.1*

