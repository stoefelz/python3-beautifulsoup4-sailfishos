#
# spec file for package python3-beautifulsoup for Mer
#

Name:           python3-beautifulsoup
Version:        4.12
Release:        1
Summary:        HTML/XML Parser for Quick-Turnaround Applications Like Screen-Scraping
License:        BSD-3-Clause
Group:          Development/Libraries/Python
Url:            http://www.crummy.com/software/BeautifulSoup/
Source:         https://www.crummy.com/software/BeautifulSoup/bs4/download/%{version}/beautifulsoup4-%{version}.0.tar.gz
#BuildRequires:  python-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}.0-build
BuildRequires:  python3-base
Requires:       python3-base
BuildArch:      noarch

%define python3_sitelib %{_libdir}/python3.?/site-packages

%description
Beautiful Soup is a Python HTML/XML parser designed for quick turnaround
projects like screen-scraping. Three features make it powerful:

* Beautiful Soup won't choke if you give it bad markup. It yields a parse tree
  that makes approximately as much sense as your original document. This is
  usually good enough to collect the data you need and run away

* Beautiful Soup provides a few simple methods and Pythonic idioms for
  navigating, searching, and modifying a parse tree: a toolkit for dissecting a
  document and extracting what you need. You don't have to create a custom
  parser for each application

* Beautiful Soup automatically converts incoming documents to Unicode and
  outgoing documents to UTF-8. You don't have to think about encodings, unless
  the document doesn't specify an encoding and Beautiful Soup can't autodetect
  one. Then you just have to specify the original encoding

Beautiful Soup parses anything you give it, and does the tree traversal stuff
for you. You can tell it "Find all the links", or "Find all the links of class
externalLink", or "Find all the links whose urls match "foo.com", or "Find the
table heading that's got bold text, then give me that text."

Valuable data that was once locked up in poorly-designed websites is now within
your reach. Projects that would have taken hours take only minutes with
Beautiful Soup.

%prep
%setup -q -n beautifulsoup4-%{version}.0

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}


%files
%defattr(-,root,root)
%{python3_sitelib}/beautifulsoup4-%{version}.0-py*.egg-info
%{python3_sitelib}/*

%changelog
