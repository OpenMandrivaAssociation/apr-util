%define build_apr_dbd_freetds 1
%define build_apr_dbd_mysql 1
%define build_apr_dbd_oracle 0
%define build_apr_dbd_pgsql 1
%define build_apr_dbd_sqlite3 1
%define build_apr_dbd_odbc 1

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

%define apuver 1
%define libname %mklibname apr-util %{apuver}
%define develname %mklibname -d apr-util

Summary:	Apache Portable Runtime Utility library
Name:		apr-util
Version:	1.3.3
Release:	%mkrel 0.1
License:	Apache License
Group:		System/Libraries
URL:		http://apr.apache.org/
Source0:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.gz
Source1:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.gz.asc
Patch0:		apr-util-1.2.2-config.diff
Patch1:		apr-util-1.2.7-link.diff
BuildRequires:	apr-devel >= 1:%{version}
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	db4-devel
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	python
BuildRequires:	readline-devel
BuildRequires:	termcap-devel
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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Obsoletes:	lib%{name} %{name}

%description -n	%{libname}
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for APR; including support
for XML, LDAP, database interfaces, URI parsing and more.

You can build %{name} with some conditional build swithes;

(ie. use with rpm --rebuild):

--with[out] apr_dbd_freetds	apr_dbd_freetds support (enabled)
--with[out] apr_dbd_mysql	apr_dbd_mysql support (enabled)
--with[out] apr_dbd_oracle	apr_dbd_oracle support (disabled)
--with[out] apr_dbd_pgsql	apr_dbd_pgsql support (enabled)
--with[out] apr_dbd_sqlite3	apr_dbd_sqlite3 support (enabled)
--with[out] apr_dbd_odbc	apr_dbd_odbc support (enabled)

%package	dbd-ldap
Summary:	DBD driver for OpenLDAP
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-ldap
DBD driver for OpenLDAP.

%if %{build_apr_dbd_pgsql}
%package	dbd-pgsql
Summary:	DBD driver for PostgreSQL
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-pgsql
DBD driver for PostgreSQL.
%endif

%if %{build_apr_dbd_mysql}
%package	dbd-mysql
Summary:	DBD driver for MySQL
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-mysql
DBD driver for MySQL.
%endif

%if %{build_apr_dbd_sqlite3}
%package	dbd-sqlite3
Summary:	DBD driver for SQLite 3
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-sqlite3
DBD driver for SQLite 3.
%endif

%if %{build_apr_dbd_freetds}
%package	dbd-freetds
Summary:	DBD driver for FreeTDS
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-freetds
DBD driver for FreeTDS.
%endif

%if %{build_apr_dbd_oracle}
%package	dbd-oracle
Summary:	DBD driver for Oracle
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-oracle
DBD driver for Oracle.
%endif

%if %{build_apr_dbd_odbc}
%package	dbd-odbc
Summary:	DBD driver for unixODBC
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-odbc
DBD driver for unixODBC.
%endif

%package -n	%{develname}
Summary:	APR utility library development kit
Group:		Development/C
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}-%{release}
Requires:	apr-util >= 1:%{version}
Requires:	openldap-devel
Requires:	expat-devel
Provides:	%{mklibname apr-util -d 1} = %{version}-%{release}
Obsoletes:	%{mklibname apr-util -d 1}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel

%description -n	%{develname}
This package provides the support files which can be used to 
build applications using the APR utility library.  The mission 
of the Apache Portable Runtime (APR) is to provide a free 
library of C data structures and routines.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 -b .config
%patch1 -p0 -b .link

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
libtoolize --copy --force; aclocal-1.7; autoconf --force
python build/gen-build.py make

%{__sed} -i -e '/OBJECTS_all/s, dbd/apr_dbd_[^ ]*\.lo,,g' build-outputs.mk

# use sqlite3 only
export apu_have_sqlite2='0'
cat >> config.cache << EOF
ac_cv_header_sqlite_h=no
ac_cv_lib_sqlite_sqlite_open=no
EOF

%configure2_5x \
    --cache-file=config.cache \
    --with-apr=%{_prefix} \
    --includedir=%{_includedir}/apr-%{apuver} \
    --with-installbuilddir=%{_libdir}/apr-%{apuver}/build \
    --enable-layout=NUX \
    --with-ldap \
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
    --without-sqlite2 \
    --with-berkeley-db \
    --without-gdbm

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
sed -ri '/^dependency_libs/{s,-l(pq|sqlite[0-9]|mysqlclient_r|rt|dl|uuid) ,,g}' \
    %{buildroot}%{_libdir}/libapr*.la

# here as well
sed -ri '/^dependency_libs/{s,%{_libdir}/lib(sqlite[0-9]|mysqlclient_r)\.la ,,g}' \
    %{buildroot}%{_libdir}/libapr*.la

# multiacrh anti-borker
perl -pi -e "s|^LDFLAGS=.*|LDFLAGS=\"\"|g" %{buildroot}%{_bindir}/apu-%{apuver}-config

# includes anti-borker
perl -pi -e "s|-I%{_includedir}/mysql||g" %{buildroot}%{_bindir}/apu-%{apuver}-config

# Unpackaged files
rm -f %{buildroot}%{_libdir}/aprutil.exp

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc CHANGES LICENSE
%{_libdir}/libaprutil-%{apuver}.so.*
%dir %{_libdir}/apr-util-%{apuver}

%files -n %{develname}
%defattr(-,root,root,-)
%doc --parents html
%attr(0755,root,root) %{_bindir}/apu-%{apuver}-config
%{_includedir}/apr-%{apuver}/*.h
%{_libdir}/libaprutil-%{apuver}.*a
%{_libdir}/libaprutil-%{apuver}.so
%{_libdir}/apr-util-%{apuver}/apr_*.*a
%{_libdir}/pkgconfig/*.pc

%files dbd-ldap
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_ldap*.so

%if %{build_apr_dbd_mysql}
%files dbd-mysql
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_mysql*.so
%endif

%if %{build_apr_dbd_pgsql}
%files dbd-pgsql
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_pgsql*.so
%endif

%if %{build_apr_dbd_sqlite3}
%files dbd-sqlite3
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_sqlite3*.so
%endif

%if %{build_apr_dbd_freetds}
%files dbd-freetds
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_freetds*.so
%endif

%if %{build_apr_dbd_oracle}
%files dbd-oracle
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_oracle*.so
%endif

%if %{build_apr_dbd_odbc}
%files dbd-odbc
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_libdir}/apr-util-%{apuver}/apr_dbd_odbc*.so
%endif
