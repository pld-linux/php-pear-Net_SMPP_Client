%define		status		devel
%define		pearname	Net_SMPP_Client
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - SMPP v3.4 client
Summary(pl.UTF-8):	%{pearname} - klient protokołu SMPP v3.4
Name:		php-pear-%{pearname}
Version:	0.4.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	49b3e65036801a8de0e9e0bccb7667d5
URL:		http://pear.php.net/package/Net_SMPP_Client/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= 4.1.0
Requires:	php-pear
Requires:	php-pear-Net_SMPP >= 0.4.1
Requires:	php-pear-Net_Socket >= 1.0.0
Requires:	php-pear-PEAR-core >= 1:1.3
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Net_SMPP_Client to korzystający z klasy Net_SMPP pakiet służacy do
komunikacji z serwerami SMPP. Może być wykorzystany między innymi do
wysyłania wiadomości SMS.

Cechy:
- stos PDU przechowujący informacje o PDU, które pojawiły się na linii
- przechowuje informacje o stanie połączenia i nie pozwoli na wysłanie
  PDU jeśli stan ten jest nieprawidłowy
- wspiera rozszerzenia SMPP

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv docs/Net_SMPP_Client/docs/examples .
mv .%{php_pear_dir}/data/Net_SMPP_Client/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/SMPP/*.php
%{_examplesdir}/%{name}-%{version}
