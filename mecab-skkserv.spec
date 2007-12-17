%define version	0.03
%define release	%mkrel 1

%define mecabversion 0.91

Name:		mecab-skkserv
Summary:	Simple server for Japanese Kana-Kanji conversion
Version:	%{version}
Release:	%{release}

# (ut) notes for licenses
# mecab-skkserv: GPL
# ipadic: NAIST license (see COPYING.IPADIC)
License:	Distributable

Group:		System/Internationalization
URL:		http://chasen.org/~taku/software/mecab/
Source0:	%{name}-%{version}.tar.bz2
Source1:	mecab-skkserv_xinetd
Requires:		mecab >= %{mecabversion}
Requires:		xinetd
BuildRequires:		mecab-devel >= %{mecabversion}
# for mecab-config:
BuildRequires:		mecab

%description
Simple server for Japanese Kana-Kanji conversion.


%prep
%setup -q

%build
%configure2_5x --libexecdir=/usr/lib --with-charset=utf8

perl -i -p -e "s/libexec/%_lib/g" Makefile
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/xinetd.d
install -c -m 0644 %{SOURCE1} %{buildroot}/etc/xinetd.d/skkserv

%clean
rm -rf $RPM_BUILD_ROOT

%post
/etc/init.d/xinetd restart

%postun
/etc/init.d/xinetd restart


%files
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.IPADIC README
%doc *.html *.css
%config(missingok,noreplace) %{_sysconfdir}/xinetd.d/skkserv
%{_bindir}/*
%_prefix/lib/mecab-skkserv/dic/ipadic/*


