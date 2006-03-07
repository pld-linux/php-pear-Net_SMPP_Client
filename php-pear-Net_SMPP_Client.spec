%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	SMPP
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}_Client

Summary:	%{_pearname} - SMPP v3.4 client
Summary(pl):	%{_pearname} - klient protoko�u SMPP v3.4
Name:		php-pear-%{_pearname}
Version:	0.3.2
Release:	1.1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b69e7d4348c03a6a59ef845825ef8749
URL:		http://pear.php.net/package/Net_SMPP_Client/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.1.0
Requires:	php-pear
Requires:	php-pear-Net_SMPP >= 0.4.1
Requires:	php-pear-Net_Socket >= 1.0.0
Requires:	php-pear-PEAR >= 1:1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net_SMPP_Client is a package for communicating with SMPP servers,
built with Net_SMPP. It can be used to send SMS messages, among other
things.

Features:
- PDU stack keeps track of which PDUs have crossed the wire
- Keeps track of the connection state, and won't let you send PDUs if
  the state is incorrect.
- Supports SMPP vendor extensions.

In PEAR status of this package is: %{_status}.

%description -l pl
Net_SMPP_Client to korzystaj�cy z klasy Net_SMPP pakiet s�u�acy do
komunikacji z serwerami SMPP. Mo�e by� wykorzystany mi�dzy innymi do
wysy�ania wiadomo�ci SMS.

Cechy:
- stos PDU przechowuj�cy informacje o PDU, kt�re pojawi�y si� na linii
- przechowuje informacje o stanie po��czenia i nie pozwoli na wys�anie
  PDU je�li stan ten jest nieprawid�owy
- wspiera rozszerzenia SMPP

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/docs/%{_pearname}/* docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
