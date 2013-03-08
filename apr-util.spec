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

%define api	1
%define major	0
%define libname %mklibname apr-util %{api} %{major}
%define devname %mklibname -d apr-util

Summary:	Apache Portable Runtime Utility library
Name:		apr-util
Version:	1.5.1
Release:	3
License:	Apache License
Group:		System/Libraries
Url:		http://apr.apache.org/
Source0:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.bz2
Source1:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.bz2.asc
Patch0:		apr-util-1.2.2-config.diff
Patch1:		apr-util-1.2.7-link.diff
Patch2:		apr-util-1.3.12-linkage_fix.diff
Patch3:		apr-util-1.5.1-no-libtool.la.patch

BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	python
BuildRequires:	pam-devel
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(apr-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(libssl)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(nspr)
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
Obsoletes:	%{_lib}apr-util1

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

%package -n	%{devname}
Summary:	APR utility library development kit
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package provides the support files which can be used to 
build applications using the APR utility library.  The mission 
of the Apache Portable Runtime (APR) is to provide a free 
library of C data structures and routines.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .config
%patch1 -p0 -b .link
%patch2 -p0 -b .linkage_fix
%patch3 -p1 -b .libtoolsucks~

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
    includedir:    %{_includedir}/apr-%{api}
    sysconfdir:    %{_sysconfdir}
    datadir:       %{_datadir}
    installbuilddir: %{_libdir}/apr-%{api}/build
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
cp %{_libdir}/apr-%{api}/build/apr_common.m4 %{_libdir}/apr-%{api}/build/find_apr.m4 %{_libdir}/apr-%{api}/build/gen-build.py build/

# conditional lib64 hack
%if "%{_lib}" != "lib"
perl -pi -e "s|/lib\b|/%{_lib}|g" build/*.m4
%endif

export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoconf --force
python build/gen-build.py make

sed -i -e '/OBJECTS_all/s, dbd/apr_dbd_[^ ]*\.lo,,g' build-outputs.mk

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
	--includedir=%{_includedir}/apr-%{api} \
	--with-installbuilddir=%{_libdir}/apr-%{api}/build \
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
	--with-crypto \
	--with-openssl=%{_prefix} \
	--with-nss=%{_prefix}

%make
make dox

%check
pushd test
    make check
popd

%install
%makeinstall_std

# Documentation
rm -rf html; cp -rp docs/dox/html html

# Remove unnecessary exports from dependency_libs
sed -ri '/^dependency_libs/{s,-l(pq|sqlite[0-9]|mysqlclient_r|rt|dl|uuid) ,,g}' %{buildroot}%{_libdir}/libapr*.la

# here as well
sed -ri '/^dependency_libs/{s,%{_libdir}/lib(sqlite[0-9]|mysqlclient_r)\.la ,,g}' %{buildroot}%{_libdir}/libapr*.la

# multiarch anti-borker
perl -pi -e "s|^LDFLAGS=.*|LDFLAGS=\"\"|g" %{buildroot}%{_bindir}/apu-%{api}-config

# includes anti-borker
perl -pi -e "s|-I%{_includedir}/mysql||g" %{buildroot}%{_bindir}/apu-%{api}-config

# Unpackaged files
rm -f %{buildroot}%{_libdir}/aprutil.exp

%files -n %{libname}
%{_libdir}/libaprutil-%{api}.so.%{major}*
%dir %{_libdir}/apr-util-%{api}

%files -n %{devname}
%doc CHANGES LICENSE
%doc --parents html
%{_bindir}/apu-%{api}-config
%{_includedir}/apr-%{api}/*.h
%{_libdir}/libaprutil-%{api}.so
%{_libdir}/pkgconfig/*.pc

%if %{build_apr_dbd_ldap}
%files dbd-ldap
%{_libdir}/apr-util-%{api}/apr_ldap*.so
%endif

%if %{build_apr_dbd_mysql}
%files dbd-mysql
%{_libdir}/apr-util-%{api}/apr_dbd_mysql*.so
%endif

%if %{build_apr_dbd_pgsql}
%files dbd-pgsql
%{_libdir}/apr-util-%{api}/apr_dbd_pgsql*.so
%endif

%if %{build_apr_dbd_sqlite3}
%files dbd-sqlite3
%{_libdir}/apr-util-%{api}/apr_dbd_sqlite3*.so
%endif

%if %{build_apr_dbd_freetds}
%files dbd-freetds
%{_libdir}/apr-util-%{api}/apr_dbd_freetds*.so
%endif

%if %{build_apr_dbd_oracle}
%files dbd-oracle
%{_libdir}/apr-util-%{api}/apr_dbd_oracle*.so
%endif

%if %{build_apr_dbd_odbc}
%files dbd-odbc
%{_libdir}/apr-util-%{api}/apr_dbd_odbc*.so
%endif

%if %{build_apr_dbm_db}
%files dbm-db
%{_libdir}/apr-util-%{api}/apr_dbm_db*.so
%endif

%files openssl
%{_libdir}/apr-util-%{api}/apr_crypto_openssl*.so

%files nss
%{_libdir}/apr-util-%{api}/apr_crypto_nss*.so

