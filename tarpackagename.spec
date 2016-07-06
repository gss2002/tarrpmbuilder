
%define rpmdesc         %(echo "$RPMDESC")

%define packagever      %{name}-%{version}
%define packagedir      %{name}
%define __jar_repack %{nil}

BuildRoot:              %{buildroot}
Summary:                %{rpmdesc}
License:                Proprietary
Name:                   %{name}
Version:                %{version}
Release:                %{release}
Source:                 %{name}-%{version}.tar.gz
Prefix:                 /usr/local/%{packagedir}
Group:                  Applications/Internet
AutoReq:                0
AutoReqProv: no


#requires:  >= 1.7.45

%description
%{rpmdesc}

%prep
%setup -q

%build
true



#%post

#%postun

%posttrans

%install
mkdir -p %{buildroot}/usr/local/%{packagedir}
cp -pR * %{buildroot}/usr/local/%{packagedir}


%files
%defattr(-,root,root)
/usr/local/%{packagedir}/*
