%define apuver 1
%define libname %mklibname apr-util %{apuver}
%define develname %mklibname -d apr-util

Summary:	Apache Portable Runtime Utility library
Name:		apr-util
Version:	1.2.12
Release:	%mkrel 3
License:	Apache License
Group:		System/Libraries
URL:		http://apr.apache.org/
Source0:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.gz
Source1:	http://www.apache.org/dist/apr/apr-util-%{version}.tar.gz.asc
# http://apache.webthing.com/database/apr_dbd_mysql.c
# http://apache.webthing.com/svn/apache/apr/apr_dbd_mysql.c
Source2:	apr_dbd_mysql.c
Patch0:		apr-util-1.2.2-config.diff
Patch2:		apr-util-postgresql.diff
Patch3:		apr-util-1.2.8-no_linkage.diff
Patch4:		apr-util-1.2.7-dso.diff
Patch5:		apr-util-1.2.7-link.diff
Patch6:		apr-util-1.2.7-apr_dbd_mysql_headers.diff
BuildRequires:	autoconf2.5
BuildRequires:	automake1.7
BuildRequires:	libtool
BuildRequires:	doxygen
BuildRequires:	apr-devel >= 1.2.12
BuildRequires:	openldap-devel
BuildRequires:	db4-devel
BuildRequires:	expat-devel
BuildRequires:	openssl-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite3-devel
BuildRequires:	python
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
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

%package	dbd-pgsql
Summary:	DBD driver for PostgreSQL
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-pgsql
DBD driver for PostgreSQL.

%package	dbd-mysql
Summary:	DBD driver for MySQL
Group:		System/Libraries
License:	GPL
Requires:	%{libname} = %{version}-%{release}

%description	dbd-mysql
DBD driver for MySQL.

%package	dbd-sqlite3
Summary:	DBD driver for SQLite 3
Group:		System/Libraries
License:	Apache License
Requires:	%{libname} = %{version}-%{release}

%description	dbd-sqlite3
DBD driver for SQLite 3.

%package -n	%{develname}
Group:		Development/C
Summary:	APR utility library development kit
Requires:	%{name} = %{version}
Requires:	%{libname} = %{version}-%{release}
Requires:	apr-util = %{version}
Requires:	apr-devel
Requires:	openldap-devel
#Requires:	db4-devel
Requires:	expat-devel
Provides:	%{libname}-devel = %{version}
Obsoletes:	%{libname}-devel
Provides:	%{name}-devel = %{version}
Obsoletes:	%{name}-devel

%description -n	%{develname}
This package provides the support files which can be used to 
build applications using the APR utility library.  The mission 
of the Apache Portable Runtime (APR) is to provide a free 
library of C data structures and routines.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0 -b .config
%patch2 -p1 -b .postgresql
%patch3 -p0 -b .exports
%patch4 -p0 -b .dso
%patch5 -p0 -b .link

cp %{SOURCE2} dbd/apr_dbd_mysql.c
%patch6 -p0 -b .mysql_headers
head -46 dbd/apr_dbd_mysql.c > LICENSE.apr_dbd_mysql

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
    --with-mysql=%{_prefix} \
    --with-pgsql=%{_prefix} \
    --without-sqlite2 \
    --with-sqlite3=%{_prefix} \
    --with-berkeley-db \
    --without-gdbm

%make
make dox

%{__make} dbd/apr_dbd_mysql.lo
libtool --mode=link --tag=CC %{__cc} -rpath %{_libdir} -avoid-version -module dbd/apr_dbd_mysql.lo -lmysqlclient_r -o dbd/apr_dbd_mysql.la

%{__make} dbd/apr_dbd_pgsql.lo
libtool --mode=link --tag=CC %{__cc} -rpath %{_libdir} -avoid-version -module dbd/apr_dbd_pgsql.lo -lpq -o dbd/apr_dbd_pgsql.la

%{__make} dbd/apr_dbd_sqlite3.lo
libtool --mode=link --tag=CC %{__cc} -rpath %{_libdir} -avoid-version -module dbd/apr_dbd_sqlite3.lo -lsqlite3 -o dbd/apr_dbd_sqlite3.la

#pushd test
#    make check
#popd

# Run the less verbose test suites
# pushd test
# make testall testrmm testdbm
# ./testall -v -q
# ./testrmm
# ./testdbm auto tsdbm
# ./testdbm -tDB auto tbdb.db
# popd

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

libtool --mode=install %{_bindir}/install -c -m 755 dbd/apr_dbd_mysql.la %{buildroot}%{_libdir}
libtool --mode=install %{_bindir}/install -c -m 755 dbd/apr_dbd_pgsql.la %{buildroot}%{_libdir}
libtool --mode=install %{_bindir}/install -c -m 755 dbd/apr_dbd_sqlite3.la %{buildroot}%{_libdir}

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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc CHANGES LICENSE
%{_libdir}/libaprutil-%{apuver}.so.*

%files -n %{develname}
%defattr(-,root,root,-)
%doc --parents html
%attr(755,root,root) %{_bindir}/apu-%{apuver}-config
%{_libdir}/libaprutil-%{apuver}.*a
%{_libdir}/libaprutil-%{apuver}.so
%{_libdir}/apr_dbd_mysql.*a
%{_libdir}/apr_dbd_pgsql.*a
%{_libdir}/apr_dbd_sqlite3.*a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/apr-%{apuver}/*.h

%files dbd-mysql
%defattr(644,root,root,755)
%doc LICENSE.apr_dbd_mysql
%attr(755,root,root) %{_libdir}/apr_dbd_mysql.so

%files dbd-pgsql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/apr_dbd_pgsql.so

%files dbd-sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/apr_dbd_sqlite3.so
