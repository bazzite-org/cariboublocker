%global gnome_version 48
%global uuid block-caribou-36@lxylxy123456.ercli.dev

Name:        gnome-shell-extension-caribou-blocker
Version:     %{gnome_version}.{{{ git_dir_version }}}
Release:     1%{?dist}
Summary:     Prevents caribou from appearing when you use a touchscreen with the on screen keyboard disabled 

Group:       User Interface/Desktops
License:     GPLv2
URL:         https://github.com/bazzite-org/cariboublocker
Source0:     %{url}/archive/refs/heads/master.tar.gz
BuildArch:   noarch

Requires:    gnome-shell >= 3.12
%description
Prevents caribou from appearing when you use a touchscreen with the on screen keyboard disabled

%prep
%autosetup -n cariboublocker-master

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 %{gnome_version}/{extension.js,metadata.json} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}
