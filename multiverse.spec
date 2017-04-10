%{?_javapackages_macros:%_javapackages_macros}
Name:           multiverse
Version:        0.7.0
Release:        6%{?dist}
Summary:        A software transactional memory implementation for the JVM

License:        ASL 2.0
URL:            http://multiverse.codehaus.org
Source0:        https://github.com/pveentjer/Multiverse/archive/multiverse-0.7.0.tar.gz
# Only the license header is included in the source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.mockito:mockito-all)

BuildArch:      noarch

%description
A software transactional memory implementation for the JVM. Access (read and
writes) to shared memory is done through transactional references, that can be
compared to the AtomicReferences of Java. Access to these references will be
done under A (atomicity), C (consistency), I (isolation) semantics.

%package javadoc
Summary:        JavaDoc for %{name}

%description javadoc
JavaDoc for %{name}.


%prep
%setup -q -n Multiverse-%{name}-%{version}

# wagon-webdav
%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :maven-deploy-plugin

cp -p %{SOURCE1} .

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.md
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Michael Simacek <msimacek@redhat.com> - 0.7.0-3
- Disable tests - they are nondeterministic

* Thu Nov 13 2014 Michael Simacek <msimacek@redhat.com> - 0.7.0-2
- Include license text

* Fri Oct 31 2014 Michael Simacek <msimacek@redhat.com> - 0.7.0-1
- Initial version
