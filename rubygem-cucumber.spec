%global ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname cucumber
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary:        Tool to execute plain-text documents as functional tests
Name:           rubygem-%{gemname}
Version:        1.0.1
Release:        1%{?dist}
Group:          Development/Languages
License:        MIT
URL:            http://cukes.info
Source0:        http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       ruby(abi) = 1.8
Requires:       rubygems
Requires:       rubygem(term-ansicolor) >= 1.0.5
Requires:       rubygem(diff-lcs) >= 1.1.2
Requires:       rubygem(builder) >= 2.1.2
Requires:       rubygem(gherkin) >= 2.4.5
Requires:       rubygem(json) >= 1.4.6
BuildRequires:  rubygems
BuildRequires:  rubygem(nokogiri) >= 1.4.4
BuildRequires:  rubygem(rspec-core) >= 2.6.0
BuildArch:      noarch
Provides:       rubygem(%{gemname}) = %{version}

%description
Cucumber lets software development teams describe how software should behave
in plain text. The text is written in a business-readable domain-specific
language and serves as documentation, automated tests and development-aid.


%prep


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{gemdir}
gem install --local --install-dir $RPM_BUILD_ROOT%{gemdir} \
        --force --rdoc %{SOURCE0}
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mv $RPM_BUILD_ROOT%{gemdir}/bin/* $RPM_BUILD_ROOT/%{_bindir}
rmdir $RPM_BUILD_ROOT%{gemdir}/bin
rm -f $RPM_BUILD_ROOT%{geminstdir}/.rvmrc
rm -f $RPM_BUILD_ROOT%{geminstdir}/.gitattributes
rm -f $RPM_BUILD_ROOT%{geminstdir}/.gitmodules
rm -f $RPM_BUILD_ROOT%{geminstdir}/.yardopts
rm -f $RPM_BUILD_ROOT%{geminstdir}/.travis.yml
rm -f $RPM_BUILD_ROOT%{geminstdir}/Gemfile.lock
rm -f $RPM_BUILD_ROOT%{geminstdir}/.rspec
find $RPM_BUILD_ROOT%{geminstdir}/bin -type f |xargs chmod a+x
find $RPM_BUILD_ROOT%{geminstdir} -type f | grep '.gitignore' | xargs rm -f

# Remove zero-length documentation files
find $RPM_BUILD_ROOT%{gemdir}/doc/%{gemname}-%{version} -empty -delete

sed -i -e "s|json_pure|json|" %{buildroot}%{geminstdir}/cucumber.gemspec
sed -i -e "s|~> 1.4.6|>= 1.1.9|" %{buildroot}%{geminstdir}/cucumber.gemspec
sed -i -e "s|json_pure|json|" %{buildroot}%{gemdir}/specifications/%{gemname}-%{version}.gemspec
sed -i -e "s|~> 1.4.6|>= 1.1.9|" %{buildroot}%{gemdir}/specifications/%{gemname}-%{version}.gemspec
sed -i -e "s|2.0.0.beta.15|1.3.0|" %{buildroot}%{gemdir}/specifications/%{gemname}-%{version}.gemspec



%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/cucumber
%dir %{geminstdir}
%{geminstdir}/bin
%{geminstdir}/features
%{geminstdir}/gem_tasks
%{geminstdir}/lib
%{geminstdir}/fixtures
%{geminstdir}/spec
%{geminstdir}/cucumber.yml
%{geminstdir}/cucumber.gemspec
%{geminstdir}/Rakefile
%doc %{geminstdir}/examples
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/History.md
%doc %{geminstdir}/README.md
%doc %{geminstdir}/Gemfile
%doc %{geminstdir}/legacy_features
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Tue Jul 12 2011 Mo Morsi <mmorsi@redhat.com> - 1.0.1-1
- update to latest upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Michal Fojtik <mfojtik@redhat.com> - 0.10.0-1
- Version bump

* Mon Sep 27 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-4
- Fixed JSON version again

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-3
- Fixed JSON version

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-2
- Fixed gherkin version in dependency list

* Fri Sep 24 2010 Michal Fojtik <mfojtik@redhat.com> - 0.9.0-1
- Version bump to match upstream
- Fixed dependency issue with new gherkin package

* Wed Aug 04 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-4
- Fixed JSON version

* Wed Aug 04 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-3
- Removed JSON patch (JSON updated in Fedora)

* Wed Aug 01 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-2
- Patched Rakefile and replaced rspec beta version dependency
- Patched Rakefile and downgraded JSON dependency

* Wed Jun 30 2010 Michal Fojtik <mfojtik@redhat.com> - 0.8.3-1
- Newer release

* Sun Oct 18 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.4.2-1
- Newer release

* Mon Oct 12 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.4.0-1
- Newer release

* Fri Jun 26 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-3
- Get rid of duplicate files (thanks to Mamoru Tasaka)

* Mon Jun 08 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-2
- Use geminstdir macro where appropriate
- Do not move examples around
- Depend on ruby(abi)
- Replace defines with globals

* Fri Jun 05 2009 Lubomir Rintel (Good Data) <lubo.rintel@gooddata.com> - 0.3.10-1
- Package generated by gem2rpm
- Move examples into documentation
- Remove empty files
- Fix up License
