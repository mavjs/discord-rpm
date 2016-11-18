%global debug_package %{nil}

# remove this when discord for linux goes stable
%define disver canary

Name:   discord
Version:    0.0.11
Release:    1%{?dist}
Summary:    Free Voice and Text Chat for Gamers.

License:    Proprietary
URL:    https://discordapp.com/
Source0:    https://dl-canary.discordapp.net/apps/linux/%{version}/%{name}-%{disver}-%{version}.tar.gz
Source1:    %{name}.desktop

ExclusiveArch:  x86_64

BuildRequires:   desktop-file-utils
Requires:   glibc, alsa-lib, GConf2, libnotify, nspr >= 4.13, nss >= 3.27
Requires:   libstdc++ >= 6, libX11 >= 1.6, libXtst >= 1.2, libappindicator

%description
All-in-one voice and text chat for gamers that’s free, secure, and works on
both your desktop and phone. Stop paying for TeamSpeak servers and hassling with
Skype. Simplify your life.

%prep
%setup -q -n DiscordCanary

%build
#nothing to build

%install
mkdir -p %{buildroot}/opt/%{name}

cp -R -p ./* %{buildroot}/opt/%{name}
chmod +x %{buildroot}/opt/%{name}/*.so

# icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -p %{name}.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
cp -p %{name}.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

# add desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%clean

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
/opt/%{name}/DiscordCanary
/opt/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Fri Nov 18 2016 Ye Myat Kaung <mavjs01@gmail.com> - 0.0.11-1
- Initial package of discord (canary) for Fedora
