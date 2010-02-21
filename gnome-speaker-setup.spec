%define name gnome-speaker-setup
%define version 0.0.0
%define git 20100221
%define rel 4
%if %{git}
%define release %mkrel 0.%{git}.%{rel}
%else
%define release %mkrel %{rel}
%endif

%define giturl git://git.0pointer.de/gnome-speaker-setup.git

Summary: GNOME speaker setup/test GUI
Name:    %{name}
Version: %{version}
Release: %{release}
License: LGPLv2+
Group:   Graphical desktop/GNOME
BuildRequires: libgnomeui2-devel
BuildRequires: vala-devel
BuildRequires: vala-tools
BuildRequires: libcanberra-devel
BuildRequires: libgee-devel
BuildRequires: pulseaudio-devel
BuildRequires: desktop-file-utils
Source0: %{name}-%{git}.tar.bz2
Source1: %{name}.desktop
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://git.0pointer.de/?p=gnome-speaker-setup.git

%description
A simple GUI to configure your speaker setup (Stereo vs 5.1 Surround etc)
and test each channel.


%prep
%setup -q -n %{name}

%build
%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m 0755 %{name} %{buildroot}%{_bindir}

desktop-file-install --vendor="" \
  --add-category="DesktopSettings" \
  --dir %{buildroot}%{_datadir}/applications %{_sourcedir}/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
