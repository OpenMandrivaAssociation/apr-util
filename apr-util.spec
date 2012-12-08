%define build_apr_dbd_ldap 1
%define build_apr_dbd_freetds 1
%define build_apr_dbd_mysql 1
%define build_apr_dbd_oracle 0
%define build_apr_dbd_pgsql 1
%define build_apr_dbd_sqlite3 1
%define build_apr_dbd_odbc 1
%define build_apr_dbm_db 1

%{?_with_apr_dbd_ldap: %{expand: %%global build_apr_dbd_ldap 1}}
%{?_without_apr_dbd_ldap: %{expand: %%global build_apr_dbd_ldap 0}}
%{?_with_apr_dbd_freetds: %{expand: %%global build_apr_dbd_freetds 1}}
%{?_without_apr_dbd_freetds: %{expand: %%global build_apr_dbd_freetds 0}}
%{?_with_apr_dbd_mysql: %{expand: %%global build_apr_dbd_mysql 1}}
%{?_without_apr_dbd_mysql: %{expand: %%global build_apr_dbd_mysql 0}}
%{?_with_apr_dbd_oracle: %{expand: %%global build_apr_dbd_oracle 1}}
%{?_without_apr_dbd_oracle: %{expand: %%global build_apr_dbd_oracle 0}}
%{?_with_apr_dbd_pgsql: %{expand: %%global build_apr_dbd_pgsql 1}}
%{?_without_apr_dbd_pgsql: %{expand: %%global build_apr_dbd_pgsql 0}}
%{?_with_apr_dbd_sqlite3: %{expand: %%global build_apr_dbd_sqlite3 1}}
%{?_without_apr_dbd_sqlite3: %{expand: %%global build_apr_dbd_sqlite3 0}}
%{?_with_apr_dbd_odbc: %{expand: %%global build_apr_dbd_odbc 1}}
%{?_without_apr_dbd_odbc: %{expand: %%global build_apr_dbd_odbc 0}}
%{?_with_apr_dbm_db: %{expand: %%global build_apr_dbm_db 1}}
%{?_without_apr_dbm_db: %{expand: %%global build_apr_dbm_db 0}}

%define apuver 1
%define libname %mklibname apr-util %{apuver}
%define develname %mklibname -d apr-util

Summary:	Apache Portable Runtime Utility library
Name:		apr-util
Version:	1.4.1
Release:	2
License:	Apache License
Group:		System/Libraries
URL:		http://apr.apache.org/
Source0:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.gz
Source1:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.gz.asc
Patch0:		apr-util-1.2.2-config.diff
Patch1:		apr-util-1.2.7-link.diff
Patch2:		apr-util-1.3.12-linkage_fix.diff
BuildRequires:	apr-devel >= 1:1.4.5
BuildRequires:	autoconf automake libtool
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	libxslt-devel
BuildRequires:	nss-devel
BuildRequires:	nspr-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	python
BuildRequires:	readline-devel
BuildRequires:	termcap-devel
%if %{build_apr_dbd_ldap}
BuildRequires:	openldap-devel
BuildRequires:	db-devel
%endif
%if %{build_apr_dbd_freetds}
BuildRequires:	freetds-devel
%endif
%if %{build_apr_dbd_mysql}
BuildRequires:	mysql-devel
%endif
%if %{build_apr_dbd_oracle}
BuildRequires:	oracle-devel
%endif
%if %{build_apr_dbd_pgsql}
BuildRequires:	postgresql-devel
%endif
%if %{build_apr_dbd_sqlite3}
BuildRequires:	sqlite3-devel
%endif
%if %{build_apr_dbd_odbc}
BuildRequires:	unixODBC-devel
%endif
%if %{build_apr_dbm_db}
BuildRequires:	db-devel
%endif

%if %{build_apr_dbd_pgsql}
# stupid postgresql... stupid build system...
# this is needed due to the postgresql packaging and due to bugs like this:
# https://qa.mandriva.com/show_bug.cgi?id=52527
%define postgresql_version %(pg_config &>/dev/null && pg_config 2>/dev/null | grep "^VERSION" | awk '{ print $4 }' 2>/dev/null || echo 0)
%endif

%description
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for APR; including support
for XML, LDAP, database interfaces, URI parsing and more.

%package -n	%{libname}
Summary:	Apache Portable Runtime Utility library
Group: 		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}
Obsoletes:	lib%{name} < %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}

%description -n	%{libname}
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for APR; including support
for XML, LDAP, database interfaces, URI parsing and more.

You can build %{name} with some conditional build swithes;

(ie. use with rpm --rebuild):

--with[out] apr_dbd_ldap	apr_dbd_ldap support (enabled)
--with[out] apr_dbd_freetds	apr_dbd_freetds support (enabled)
--with[out] apr_dbd_mysql	apr_dbd_mysql support (enabled)
--with[out] apr_dbd_oracle	apr_dbd_oracle support (disabled)
--with[out] apr_dbd_pgsql	apr_dbd_pgsql support (enabled)
--with[out] apr_dbd_sqlite3	apr_dbd_sqlite3 support (enabled)
--with[out] apr_dbd_odbc	apr_dbd_odbc support (enabled)
--with[out] apr_dbm_db		apr_dbm_db support (enabled)

%if %{build_apr_dbd_ldap}
%package	dbd-ldap
Summary:	DBD driver for OpenLDAP
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}

%description	dbd-ldap
DBD driver for OpenLDAP.
%endif

%if %{build_apr_dbd_pgsql}
%package	dbd-pgsql
Summary:	DBD driver for PostgreSQL
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}
Requires:	postgresql-libs >= %{postgresql_version}

%description	dbd-pgsql
DBD driver for PostgreSQL.
%endif

%if %{build_apr_dbd_mysql}
%package	dbd-mysql
Summary:	DBD driver for MySQL
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}

%description	dbd-mysql
DBD driver for MySQL.
%endif

%if %{build_apr_dbd_sqlite3}
%package	dbd-sqlite3
Summary:	DBD driver for SQLite 3
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}

%description	dbd-sqlite3
DBD driver for SQLite 3.
%endif

%if %{build_apr_dbd_freetds}
%package	dbd-freetds
Summary:	DBD driver for FreeTDS
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}

%description	dbd-freetds
DBD driver for FreeTDS.
%endif

%if %{build_apr_dbd_oracle}
%package	dbd-oracle
Summary:	DBD driver for Oracle
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}

%description	dbd-oracle
DBD driver for Oracle.
%endif

%if %{build_apr_dbd_odbc}
%package	dbd-odbc
Summary:	DBD driver for unixODBC
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}

%description	dbd-odbc
DBD driver for unixODBC.
%endif

%if %{build_apr_dbm_db}
%package	dbm-db
Summary:	DBD driver for Berkley BD
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} >= %{version}-%{release}

%description	dbm-db
DBD driver for Berkley BD.
%endif

%package	openssl
Summary:	APR utility library OpenSSL crypto support
Group:		System/Libraries
Requires:	%{libname} >= %{version}-%{release}

%description	openssl
This package provides the OpenSSL crypto support for apr-util.

%package	nss
Summary:	APR utility library NSS crypto support
Group:		System/Libraries
Requires:	%{libname} >= %{version}-%{release}

%description	nss
This package provides the NSS crypto support for apr-util.

%package -n	%{develname}
Summary:	APR utility library development kit
Group:		Development/C
Requires:	%{name} >= %{version}
Requires:	%{libname} >= %{version}-%{release}
Requires:	apr-util = %{version}
Requires:	apr-devel
Requires:	openldap-devel
Requires:	expat-devel
Provides:	%{mklibname apr-util -d 1} = %{version}-%{release}
Obsoletes:	%{mklibname apr-util -d 1} < %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < %{version}-%{release}

%description -n	%{develname}
This package provides the support files which can be used to 
build applications using the APR utility library.  The mission 
of the Apache Portable Runtime (APR) is to provide a free 
library of C data structures and routines.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .config
%patch1 -p0 -b .link
%patch2 -p0 -b .linkage_fix

cat >> config.layout << EOF
<Layout NUX>
    prefix:        %{_prefix}
    exec_prefix:   %{_prefix}
    bindir:        %{_bindir}
    sbindir:       %{_sbindir}
    libdir:        %{_libdir}
    libexecdir:    %{_libexecdir}
    mandir:        %{_mandir}
    infodir:       %{_infodir}
    includedir:    %{_includedir}/apr-%{apuver}
    sysconfdir:    %{_sysconfdir}
    datadir:       %{_datadir}
    installbuilddir: %{_libdir}/apr-%{apuver}/build
    localstatedir: /var
    runtimedir:    /var/run
    libsuffix:     -\${APRUTIL_MAJOR_VERSION}
</Layout>
EOF

%build
%serverbuild

# We need to re-run ./buildconf because of any applied patch(es)
#./buildconf --with-apr=%{_prefix}

# buildconf is borked...
cp %{_libdir}/apr-%{apuver}/build/apr_common.m4 %{_libdir}/apr-%{apuver}/build/find_apr.m4 %{_libdir}/apr-%{apuver}/build/gen-build.py build/

# conditional lib64 hack
%if "%{_lib}" != "lib"
perl -pi -e "s|/lib\b|/%{_lib}|g" build/*.m4
%endif

export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoconf --force
python build/gen-build.py make

%{__sed} -i -e '/OBJECTS_all/s, dbd/apr_dbd_[^ ]*\.lo,,g' build-outputs.mk

# force values that may produce wrong results
export apu_have_sqlite2='0'
cat >> config.cache << EOF
ac_cv_header_sqlite_h=no
ac_cv_lib_sqlite_sqlite_open=no
ac_cv_ldap_set_rebind_proc_style=three
EOF

%configure2_5x \
    --cache-file=config.cache \
    --with-apr=%{_prefix} \
    --includedir=%{_includedir}/apr-%{apuver} \
    --with-installbuilddir=%{_libdir}/apr-%{apuver}/build \
    --enable-layout=NUX \
%if %{build_apr_dbd_ldap}
    --with-ldap \
%endif
%if %{build_apr_dbd_freetds}
    --with-freetds=%{_prefix} \
%endif
%if %{build_apr_dbd_mysql}
    --with-mysql=%{_prefix} \
%endif
%if %{build_apr_dbd_oracle}
    --with-oracle \
%endif
%if %{build_apr_dbd_pgsql}
    --with-pgsql=%{_prefix} \
%endif
%if %{build_apr_dbd_sqlite3}
    --with-sqlite3=%{_prefix} \
%endif
%if %{build_apr_dbd_odbc}
    --with-odbc=%{_prefix} \
%endif
%if %{build_apr_dbm_db}
    --with-berkeley-db \
%endif
    --without-sqlite2 \
    --without-gdbm \
    --with-crypto --with-openssl=%{_prefix} --with-nss=%{_prefix}

%make
make dox

%check
pushd test
    make check
popd

%install
rm -rf %{buildroot}

%makeinstall_std

# Documentation
rm -rf html; cp -rp docs/dox/html html

# Remove unnecessary exports from dependency_libs
sed -ri '/^dependency_libs/{s,-l(pq|sqlite[0-9]|mysqlclient_r|rt|dl|uuid) ,,g}' %{buildroot}%{_libdir}/libapr*.la

# here as well
sed -ri '/^dependency_libs/{s,%{_libdir}/lib(sqlite[0-9]|mysqlclient_r)\.la ,,g}' %{buildroot}%{_libdir}/libapr*.la

# multiarch anti-borker
perl -pi -e "s|^LDFLAGS=.*|LDFLAGS=\"\"|g" %{buildroot}%{_bindir}/apu-%{apuver}-config

# includes anti-borker
perl -pi -e "s|-I%{_includedir}/mysql||g" %{buildroot}%{_bindir}/apu-%{apuver}-config

# Unpackaged files
rm -f %{buildroot}%{_libdir}/aprutil.exp

%files -n %{libname}
%doc CHANGES LICENSE
%{_libdir}/libaprutil-%{apuver}.so.*
%dir %{_libdir}/apr-util-%{apuver}

%files -n %{develname}
%doc --parents html
%attr(0755,root,root) %{_bindir}/apu-%{apuver}-config
%{_includedir}/apr-%{apuver}/*.h
%{_libdir}/libaprutil-%{apuver}.so
%{_libdir}/pkgconfig/*.pc

%if %{build_apr_dbd_ldap}
%files dbd-ldap
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_ldap*.so
%endif

%if %{build_apr_dbd_mysql}
%files dbd-mysql
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_mysql*.so
%endif

%if %{build_apr_dbd_pgsql}
%files dbd-pgsql
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_pgsql*.so
%endif

%if %{build_apr_dbd_sqlite3}
%files dbd-sqlite3
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_sqlite3*.so
%endif

%if %{build_apr_dbd_freetds}
%files dbd-freetds
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_freetds*.so
%endif

%if %{build_apr_dbd_oracle}
%files dbd-oracle
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_oracle*.so
%endif

%if %{build_apr_dbd_odbc}
%files dbd-odbc
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_odbc*.so
%endif

%if %{build_apr_dbm_db}
%files dbm-db
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbm_db*.so
%endif

%files openssl
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_crypto_openssl*.so

%files nss
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_crypto_nss*.so

%changelog
* Wed Feb 01 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-0.1
- built for updates

* Wed Feb 01 2012 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-2mdv2012.0
+ Revision: 770376
- make it backportable

* Sun Dec 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-1
+ Revision: 743527
- 1.4.1
- various fixes

* Thu Dec 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.12-4
+ Revision: 739189
- rebuilt for new unixODBC (second try)
- rebuilt for new unixODBC

* Tue Nov 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.12-2
+ Revision: 735462
- fix build
- drop the static libs and the libtool *.la files
- various cleanups

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.12-1
+ Revision: 676498
- 1.3.12

* Fri May 20 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.12-0
+ Revision: 676365
- 1.3.12 (pre-release)

* Mon May 09 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.11-1
+ Revision: 672986
- 1.3.11
- drop the db51 patch, it was added upstream

* Wed Mar 30 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3.10-10
+ Revision: 649270
- rebuild against new db 5.1.25

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-9
+ Revision: 645740
- relink against libmysqlclient.so.18

* Tue Mar 01 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-8
+ Revision: 641085
- rebuilt against bdb 5.1

* Sun Jan 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-7mdv2011.0
+ Revision: 627558
- added db51 m4 logic from svn
- don't force the usage of automake1.7

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-6mdv2011.0
+ Revision: 627017
- rebuilt against mysql-5.5.8 libs, again

* Tue Dec 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-5mdv2011.0
+ Revision: 625577
- rebuilt against mysql-5.5.8 libs

* Wed Dec 01 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.3.10-4mdv2011.0
+ Revision: 604582
- Rebuild with newer apr-devel

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-3mdv2011.0
+ Revision: 601021
- rebuild

* Wed Oct 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-2mdv2011.0
+ Revision: 583712
- stupid build system
- 1.3.10 (final)

* Sat Oct 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.10-0.1mdv2011.0
+ Revision: 582560
- 1.3.10 (re-release)

* Thu Feb 18 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.9-3mdv2010.1
+ Revision: 507457
- rebuild

* Wed Dec 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.9-2mdv2010.1
+ Revision: 484240
- fix db48 linkage

* Thu Aug 06 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.9-1mdv2010.0
+ Revision: 410950
- 1.3.9

* Wed Aug 05 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.9-0.1mdv2010.0
+ Revision: 409999
- 1.3.9

* Sat Aug 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.8-3mdv2010.0
+ Revision: 406064
- make sure the latest postgresql libs are used

* Fri Jul 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.8-2mdv2010.0
+ Revision: 396723
- rebuild

* Tue Jul 07 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.8-1mdv2010.0
+ Revision: 393172
- 1.3.8 (final)
- 1.3.8 (pre-release)

* Fri Jun 05 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.7-1mdv2010.0
+ Revision: 383064
- 1.3.7 (final)

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.7-0.1mdv2010.0
+ Revision: 382673
- 1.3.7 (release candidate)
- nuke upstream patches

* Sun Mar 22 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-9mdv2009.1
+ Revision: 360371
- added P5 that fixes ASF PR45679
- added P6 that fixes ASF PR46012
- added P7 that fixes ASF PR23356
- added P8 that fixes a number of upstream bugs, (P3 fixed ASF
  PR46482, P4 fixed ASF PR46588)

* Sun Feb 22 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-8mdv2009.1
+ Revision: 343926
- added two upstream patches to fix bugs in apr_memcache.c (P3,P4)

* Wed Feb 18 2009 Michael Scherer <misc@mandriva.org> 1.3.4-7mdv2009.1
+ Revision: 342647
- rebuild for db 4.6, as we are currently linked with db4.7, this cause problem on
  upgrade and prevent installation of rpm-devel and apache-devel at the same time

* Sat Feb 14 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-6mdv2009.1
+ Revision: 340270
- use P2 from upstream svn

* Wed Feb 11 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-5mdv2009.1
+ Revision: 339506
- fix segfault in the freetds driver (P2, Bojan Smojver)

* Wed Dec 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-4mdv2009.1
+ Revision: 315099
- revert the last "too late at night" change
- enforce system libtool

* Mon Dec 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-3mdv2009.1
+ Revision: 314473
- rediff some patches to meet the nofuzz criteria
- rebuilt against db4.7 and mysql-5.1.30 libs

* Tue Sep 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2mdv2009.0
+ Revision: 278890
- rebuild

* Sun Aug 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-1mdv2009.0
+ Revision: 272947
- 1.3.4 (final)

* Thu Aug 14 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-0.1mdv2009.0
+ Revision: 271799
- fix deps
- 1.3.4

* Sun Aug 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-0.2mdv2009.0
+ Revision: 270189
- fix deps

* Sat Aug 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-0.1mdv2009.0
+ Revision: 270069
- 1.3.3 (dev rel)
- fix deps
- drop redundant patches

* Mon Jun 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-2mdv2009.0
+ Revision: 228076
- rebuilt due to PayloadIsLzma problems

* Sat Jun 21 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-1mdv2009.0
+ Revision: 227723
- 1.3.2 (release)

* Tue Jun 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-0.1mdv2009.0
+ Revision: 223215
- 1.3.2 (unreleased)
- drop the freetds_fix patch, it's implemented upstream

* Mon Jun 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2009.0
+ Revision: 219531
- fix freetds from HEAD
- added conditional build stuff

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jun 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2009.0
+ Revision: 216699
- bump release

* Thu Jun 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-0.2mdv2009.0
+ Revision: 215196
- more dep fixes
- added P2 to make it find the postgresql headers
- fix deps
- fix deps (will fix freetds_mssql later)
- 1.3.0
- drop S2 (mysql support) as it's included and re-licensed.
- drop upstream implemented patches; P2,P3,P4
- renumbered patches (P5 -> P1)
- drop the pld libtool fiddle magic, a better fix is implemented

* Wed May 28 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-6mdv2009.0
+ Revision: 212789
- rebuild

* Sat May 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-5mdv2009.0
+ Revision: 208457
- rebuild
- fix deps

* Thu Jan 24 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-4mdv2008.1
+ Revision: 157327
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild with fixed %%serverbuild macro

* Fri Dec 21 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-2mdv2008.1
+ Revision: 136281
- rebuilt against new build deps

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.12-1mdv2008.1
+ Revision: 113581
- 1.2.12
- rediffed P3

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-1mdv2008.0
+ Revision: 80714
- 1.2.10 (release)

* Wed Sep 05 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.10-0.1mdv2008.0
+ Revision: 79881
- 1.2.10
- drop P1, not needed anymore
- new apr_dbd_mysql.c

* Sat Aug 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-7mdv2008.0
+ Revision: 65566
- really use the new devel package naming (duh!)

* Sat Aug 18 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-6mdv2008.0
+ Revision: 65565
- use the new devel package naming
- fix BuildPrereq rpmlint errors

* Sat Jun 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-5mdv2008.0
+ Revision: 43404
- use the new %%serverbuild macro

* Thu Jun 07 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-4mdv2008.0
+ Revision: 36657
- use distro conditional -fstack-protector


* Sat Jan 27 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-3mdv2007.0
+ Revision: 114291
- new version of apr_dbd_mysql.c with clearified license too

* Fri Jan 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-2mdv2007.1
+ Revision: 110700
- rebuilt against new postgresql libs

* Sun Dec 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-1mdv2007.1
+ Revision: 94535
- 1.2.8
- rediffed patches; P2,P3
- drop upstream patches; P7,P8

* Thu Nov 16 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-10mdv2007.1
+ Revision: 84755
- sync with fedora (1.2.7-4)
- new apr_dbd_mysql.c (better 5.x support)
- Import apr-util

* Tue Sep 05 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-9mdv2007.0
- rebuilt against MySQL-5.0.24a-1mdv2007.0 due to ABI changes

* Tue Jul 18 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-8mdk
- rebuild

* Tue Jul 18 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-7mdk
- rebuild

* Tue Jul 18 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-6mdk
- make it build (P6)

* Tue Jul 18 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-5mdk
- new apr_dbd_mysql (S2)

* Wed Jul 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-4mdk
- rebuild

* Mon May 01 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-3mdk
- added PLD patches and spec file magic (P3,P4)
- new apr_dbd_mysql (S2)

* Mon May 01 2006 Stefan van der Eijk <stefan@eijk.nu> 1.2.7-2mdk
- rebuild for sparc

* Sat Apr 15 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-1mdk
- 1.2.7

* Thu Mar 30 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-1mdk
- 1.2.6

* Tue Mar 21 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.5-1mdk
- 1.2.5

* Wed Dec 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdk
- fix deps (spturtle)

* Mon Dec 12 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- 1.2.2
- merge with the apr package from contrib
- merge fedora changes (1.2.2-2)

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-3mdk
- rebuilt to provide a -debug package too

* Mon Oct 17 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-2mdk
- rebuild

* Tue Oct 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-1mdk
- 0.9.7
- drop upstream patches; P8

* Tue Sep 06 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-8mdk
- rebuild

* Wed Aug 31 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.9.6-7mdk
- Rebuild for libldap2.3

* Sun Jun 12 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-6mdk
- rebuilt against new openldap and sasl libs
- enable gdbm linkage

* Tue May 17 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.6-5mdk
- added P8 for apr_memcache

* Fri Mar 18 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.6-4mdk
- use the %%mkrel macro

* Wed Feb 23 2005 Stefan van der Eijk <stefan@eijk.nu> 0.9.6-3mdk
- Remove "Requires: db4-devel" from -devel package #13906

* Mon Feb 07 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.6-2mdk
- rebuilt against new ldap libs

* Mon Feb 07 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.6-1mdk
- 0.9.6

* Fri Feb 04 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.9.5-16mdk
- rebuild for ldap2.2_7

* Thu Jan 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-15mdk
- run the tests before %%makeinstall_std
- misc spec file fixes

* Tue Jan 11 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-14mdk
- make --with debug work

* Thu Jan 06 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-13mdk
- lib64 fixes

* Wed Dec 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-12mdk
- revert latest "lib64 fixes"

* Wed Dec 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-11mdk
- lib64 fixes

* Thu Nov 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-10mdk
- 0.9.5

* Thu Sep 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-9mdk
- new P0
- drop P100, it's included

* Thu Sep 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-8mdk
- security fix (P100) for CAN-2004-0786

* Wed Aug 11 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-7mdk
- rebuilt against db4.2

* Thu Jul 01 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-6mdk
- new P0
- drop P3,P4,P6 and P8 the fix is implemented upstream
- drop P5, another fix is implemented upstream
- fix P7, it's partially implemented upstream

* Fri Jun 18 2004 Jean-Michel Dault <jmdault@mandrakesoft.com> 0.9.5-5mdk
- rebuild with new openssl

* Fri Jun 18 2004 Jean-Michel Dault <jmdault@mandrakesoft.com> 0.9.5-4mdk
- rebuild

* Wed May 19 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-2mdk
- rebuild

* Sat May 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.9.5-1mdk
- initial fedora import and mandrake adaptions

* Fri Apr 02 2004 Joe Orton <jorton@redhat.com> 0.9.4-14
- fix use of SHA1 passwords (#119651)

* Wed Mar 31 2004 Joe Orton <jorton@redhat.com> 0.9.4-13
- remove fundamentally broken check_sbcs() from xlate code

* Fri Mar 19 2004 Joe Orton <jorton@redhat.com> 0.9.4-12
- tweak xlate fix

* Fri Mar 19 2004 Joe Orton <jorton@redhat.com> 0.9.4-11
- rebuild with xlate fixes and tests enabled

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com> 0.9.4-10.1
- rebuilt

* Tue Mar 02 2004 Joe Orton <jorton@redhat.com> 0.9.4-10
- rename sdbm_* symbols to apu__sdbm_*

* Mon Feb 16 2004 Joe Orton <jorton@redhat.com> 0.9.4-9
- fix sdbm apr_dbm_exists() on s390x/ppc64

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 0.9.4-8
- rebuilt

* Thu Feb 05 2004 Joe Orton <jorton@redhat.com> 0.9.4-7
- fix warnings from use of apr_optional*.h with gcc 3.4

* Thu Jan 29 2004 Joe Orton <jorton@redhat.com> 0.9.4-6
- drop gdbm support

