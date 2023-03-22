# $Revision: 1.10 $, $Date: 2012/04/07 12:00:10 $
Summary:	The open source monitoring and reporting tool for Bacula
Name:		bacula-web
Provides:	bacula-web-%{version}
Release:	1
License:	GPLv2
Version:	%{version}

Group:		Applications/System
URL:		http://www.bacula-web.org/

#Source0:	https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz

BuildRequires:  composer

Requires: 	php >= 7.4.0
Requires:	php-common
Requires:	php-gettext
Requires:	php-pdo
Requires:	webserver(php)

BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_httpdroot	/var/www/html
%define		_appdir		%{_httpdroot}/%{name}
%define		_wwwpubdir	%{_httpdroot}/%{name}/public
%define		_confdir	%{_appdir}/application/config
%define		_cachedir	%{_appdir}/application/views/cache
%define		_localedir	%{_appdir}/application/locale
%define		_docsdir	%{_appdir}/docs

%description
Bacula-Web is a web based tool written in PHP that provide you a
summarized view of your bacula's backup infrastructure. It obtain his
information from your bacula catalog's database.

%prep
%setup -c -D

%install
%{__install} -m 755 -d $RPM_BUILD_ROOT%{_httpdroot}/%{name}
%{__cp} -dR %{name}-%{version}/* $RPM_BUILD_ROOT%{_httpdroot}/%{name}

%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/CHANGELOG.md
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/CODE_OF_CONDUCT.md
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/CONTRIBUTING.md
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/LICENSE
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/README.md
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/SECURITY.md
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/phpunit.xml
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/release-please-config.json
%{__rm} $RPM_BUILD_ROOT%{_httpdroot}/%{name}/sonar-project.properties
%{__rm} -rf $RPM_BUILD_ROOT%{_httpdroot}/%{name}/tests

cd $RPM_BUILD_ROOT%{_httpdroot}/%{name} && composer install --no-dev

%{__rm} -r $RPM_BUILD_ROOT%{_httpdroot}/%{name}/composer.*

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

#%config %{_confdir}/config.php

%docdir %{_docsdir}
%{_docsdir}

%dir %{_appdir}
%{_appdir}/public/index.php
%{_appdir}/public/.htaccess
%{_appdir}/console.php
%{_appdir}/bwc
%{_appdir}/vendor

%dir %{_wwwpubdir}
%{_wwwpubdir}/css
%{_wwwpubdir}/js
%{_wwwpubdir}/img
%{_wwwpubdir}/webfonts
%{_wwwpubdir}/fonts

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

#%dir %attr(775,http,http) %{_cachedir}

%define date %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%changelog

* Mon Aug 28 2017 - bacula-dev@dflc.ch
- First rpm spec file version 
