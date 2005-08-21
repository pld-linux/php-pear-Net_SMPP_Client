%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	SMPP
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}_Client

Summary:	%{_pearname} - SMPP v3.4 client
Summary(pl):	%{_pearname} - klient protoko³u SMPP v3.4
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b69e7d4348c03a6a59ef845825ef8749
URL:		http://pear.php.net/package/Net_SMPP_Client/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_SMPP_Client is a package for communicating with SMPP servers, built
with Net_SMPP. It can be used to send SMS messages, among other things.

Features:
- PDU stack keeps track of which PDUs have crossed the wire
- Keeps track of the connection state, and won't let you send PDUs if
  the state is incorrect.
- Supports SMPP vendor extensions.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_SMPP_Client to korzystaj±cy z klasy Net_SMPP pakiet s³u¿acy do
komunikacji z serwerami SMPP. Mo¿e byæ wykorzystany miêdzy innymi do
wysy³ania wiadomo¶ci SMS.

Cechy:
- stos PDU przechowuj±cy informacje o PDU, które pojawi³y siê na linii
- przechowuje informacje o stanie po³±czenia i nie pozwoli na wys³anie
  PDU je¶li stan ten jest nieprawid³owy
- wspiera rozszerzenia SMPP

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Client

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
