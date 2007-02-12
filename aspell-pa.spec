Summary:	Panjabi dictionary for aspell
Summary(pl.UTF-8):   Słownik pendżabski dla aspella
Name:		aspell-pa
Version:	0.01
%define	subv	1
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/pa/aspell6-pa-%{version}-%{subv}.tar.bz2
# Source0-md5:	de336d6ef55ad6fa81f8903765c6c95d
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Panjabi dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik pendżabski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-pa-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
