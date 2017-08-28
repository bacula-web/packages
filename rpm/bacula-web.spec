# $Revision: 1.10 $, $Date: 2012/04/07 12:00:10 $
Summary:	The open source monitoring and reporting tool for Bacula
Name:		bacula-web
Provides:	bacula-web-%{version}
Release:	1
License:	GPLv2

Group:		Applications/System
URL:		http://www.bacula-web.org/

Source0:	http://www.bacula-web.org/tl_files/downloads/%{name}-%{version}.tar.gz
Requires: 	php >= 5.6.0
Requires:	php-common
Requires:	php-gd
Requires:	php-gettext
Requires:	php-pdo
Requires:	webserver(php)

BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_httpdroot	/var/www/html
%define		_appdir		%{_httpdroot}/%{name}
%define		_confdir	%{_appdir}/application/config
%define		_cachedir	%{_appdir}/application/view/cache
%define		_localedir	%{_appdir}/application/locale
%define		_docsdir	%{_appdir}/docs

%description
Bacula-Web is a web based tool written in PHP that provide you a
summarized view of your bacula's backup infrastructure. It obtain his
information from your bacula catalog's database.

%prep
%setup -qc

%install
%{__install} -m 755 -d $RPM_BUILD_ROOT%{_httpdroot}/%{name}
%{__cp} -dR * $RPM_BUILD_ROOT%{_httpdroot}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT
# cleanup cache from previous rpm
echo %{_cachedir}/* | xargs rm -f

%preun
if [ "$1" = 0 ]; then
	echo %{_cachedir}/* | xargs rm -f
fi

%files
%{_appdir}/core
%{_appdir}/application

%defattr(644,root,root,755)

%config %{_confdir}/config.php.sample

%docdir %{_docsdir}
%{_docsdir}

%dir %{_appdir}
%{_appdir}/backupjob-report.php
%{_appdir}/client-report.php
%{_appdir}/index.php
%{_appdir}/jobs.php
%{_appdir}/pools.php
%{_appdir}/test.php
%{_appdir}/joblogs.php


#%dir %{_appdir}/core
#%{_appdir}/core/bweb.class.php
#%{_appdir}/core/db
#%_appdir}/core/graph
#%{_appdir}/core/i18n
#%{_appdir}/core/utils

#%dir %{_localedir}
#%lang(de) %{_localedir}/de_DE
#%lang(en) %{_localedir}/en_EN
#%lang(es) %{_localedir}/es_ES
#%lang(fr) %{_localedir}/fr_FR
#%lang(it) %{_localedir}/it_IT
#%lang(sv) %{_localedir}/sv_SV
#%lang(nl) %{_localedir}/nl_NL
#%lang(br) %{_localedir}/pt_BR

%dir %attr(775,http,http) %{_cachedir}

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%changelog

* Mon Aug 28 2017 - bacula-dev@dflc.ch
- First rpm spec file version 
