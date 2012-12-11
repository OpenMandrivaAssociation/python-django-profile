%define realname django-profile
%define name    python-%{realname}
%define version 0.6
%define release %mkrel 1
%define vcsdate 20090813
%define vcstag r420

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Django pluggable user profile zone
Group:          Development/Python
License:        BSD
URL:            http://code.google.com/p/django-profile/
Source:         %{realname}-%{version}-%{vcstag}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django python-imaging

%description
This is a user private zone/profile management application, allowing
the user to take control of his account and insert information about
him in his profile.

Inside this package you will find a demo application which will show
you what can be accomplished with the rest of the utilities included
in the package.

%prep
%setup -q -n %{realname}-%{version}-%{vcstag}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# delete unpackaged files
rm -rf %{buildroot}%{py_puresitedir}/demo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc INSTALL.txt CHANGELOG.txt LICENSE.txt README.txt TODO.txt demo/
%{py_puresitedir}/*


%changelog
* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6-1mdv2011.0
+ Revision: 591995
- add BR python-setuptools
- import python-django-profile

