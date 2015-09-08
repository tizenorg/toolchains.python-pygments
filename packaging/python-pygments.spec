%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-pygments
Version:        1.1.1
Release:        1
Summary:        A syntax highlighting engine written in Python

Group:          Development/Libraries
License:        BSD
URL:            http://pygments.org/
Source0:        http://cheeseshop.python.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
Requires:       python-setuptools


%description
Pygments is a syntax highlighting engine written in Python. That means, it 
will take source code (or other markup) in a supported language and output 
a processed version (in different formats) containing syntax highlighting 
markup.


%prep
%setup -q -n Pygments-%{version}


%build
%{__python} setup.py build
%{__sed} -i 's/\r//' LICENSE


%install

%if 0%{?suse_version}
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot} --record-rpm=INSTALLED_FILES  
%else
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --prefix=%{_prefix}
%endif

%if 0%{?suse_version}
%files -f INSTALLED_FILES
%else
%files
%{python_sitelib}/*
%endif
# For noarch packages: sitelib
%{_bindir}/pygmentize


