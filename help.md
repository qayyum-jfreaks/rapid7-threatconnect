# Description

WhoisFreaks (https://www.whoisfreaks.com) Unleash the Power of Data with Our Domain and IP Intelligence Gain real-time DNS, domain, and IP intelligence to strengthen security, protect your brand, and drive smarter decisions with our advanced data platform

# Key Features

* WHOIS
* Domain Lookup
* Brand Monitor
* IP Lookup
* DNS Lookup

# Requirements

* Requires an API Key from WhoisFreaks

# Supported Product Versions

* WhoisFreaks_api v3.4, v3.3, v2.0, v1.0

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|string|None|True|WhoisFreaks API key (sent as X-API-KEY header)|None|your_api_key_here|None|None|

Example input:

```
{
  "api_key": "your_api_key_here"
}
```

## Technical Details

### Actions


#### ASN WHOIS

This action is used to perform a WHOIS lookup for an Autonomous System Number

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asn|string|None|True|Autonomous System Number with or without the as prefix|None|AS15169|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
  
Example input:

```
{
  "asn": "AS15169",
  "format": "json"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|ASN WHOIS record|None|
  
Example output:

```
{
  "response": {}
}
```

#### Bulk DNS

This action is used to perform live DNS lookups for multiple domains or IPs in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|type|string|None|True|DNS record type to query|["a", "aaaa", "mx", "cname", "ns", "txt", "soa"]|a|None|None|
|values|[]string|None|True|List of domains or IPs to query|None|["example.com", "example.org"]|None|None|
  
Example input:

```
{
  "format": "json",
  "type": "a",
  "values": [
    "example.com",
    "example.org"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Bulk DNS result|None|
  
Example output:

```
{
  "response": {}
}
```

#### Bulk Domain Availability

This action is used to check availability for up to 100 domains in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domains|[]string|None|True|List of domain names (max 100)|None|["example.com", "example.org"]|None|None|
  
Example input:

```
{
  "domains": [
    "example.com",
    "example.org"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Bulk domain availability result|None|
  
Example output:

```
{
  "response": {}
}
```

#### Bulk IP Geolocation

This action is used to retrieve geolocation data for multiple IPs in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ips|[]string|None|True|List of IPv4 or IPv6 addresses|None|["8.8.8.8", "1.1.1.1"]|None|None|
  
Example input:

```
{
  "ips": [
    "8.8.8.8",
    "1.1.1.1"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Bulk IP geolocation result|None|
  
Example output:

```
{
  "response": {}
}
```

#### Bulk IP Reputation

This action is used to retrieve reputation scores for multiple IPs in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ips|[]string|None|True|List of IPv4 or IPv6 addresses|None|["8.8.8.8", "1.1.1.1"]|None|None|
  
Example input:

```
{
  "ips": [
    "8.8.8.8",
    "1.1.1.1"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Bulk IP reputation result|None|
  
Example output:

```
{
  "response": {}
}
```

#### Bulk IP Security

This action is used to retrieve security intelligence for multiple IPs in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ips|[]string|None|True|List of IPv4 or IPv6 addresses|None|["8.8.8.8", "1.1.1.1"]|None|None|
  
Example input:

```
{
  "ips": [
    "8.8.8.8",
    "1.1.1.1"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Bulk IP security result|None|
  
Example output:

```
{
  "response": {}
}
```

#### Bulk WHOIS

This action is used to fetch WHOIS records for up to 100 domains in one request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domains|[]string|None|True|List of domain names (max 100)|None|["example.com", "example.org"]|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
  
Example input:

```
{
  "domains": [
    "example.com",
    "example.org"
  ],
  "format": "json"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Bulk WHOIS result|None|
  
Example output:

```
{
  "response": {}
}
```

#### DNS Lookup

This action is used to perform a live DNS lookup for a domain or IP address - at least one of domainName or ipAddress 
is required

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|False|Domain name for DNS lookup|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|ipAddress|string|None|False|IP address for reverse DNS PTR lookup|None|8.8.8.8|None|None|
|type|string|None|False|DNS record type such as A, AAAA, MX, NS, TXT, or all|None|all|None|None|
  
Example input:

```
{
  "domainName": "example.com",
  "format": "json",
  "ipAddress": "8.8.8.8",
  "type": "all"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|DNS records|None|
  
Example output:

```
{
  "response": {}
}
```

#### Domain Availability

This action is used to check whether a domain is available for registration

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|True|Domain name to check|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
  
Example input:

```
{
  "domainName": "example.com",
  "format": "json"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Domain availability result|None|
  
Example output:

```
{
  "response": {}
}
```

#### Domain Reputation

This action is used to retrieve the threat score and reputation assessment for a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|True|Domain to assess - must contain at least one dot and be at most 253 characters|None|example.com|None|None|
  
Example input:

```
{
  "domainName": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Domain reputation and risk assessment|None|
  
Example output:

```
{
  "response": {}
}
```

#### Historical DNS

This action is used to retrieve historical DNS records for a domain (paginated)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|True|Domain name to query historical DNS for|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
|type|string|None|False|DNS record type filter such as A, AAAA, MX, NS, TXT, SOA, or CNAME|None|A|None|None|
  
Example input:

```
{
  "domainName": "example.com",
  "format": "json",
  "page": 1,
  "type": "A"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]object|False|List of historical DNS records|None|
  
Example output:

```
{
  "response": [
    {}
  ]
}
```

#### Historical WHOIS

This action is used to retrieve historical WHOIS records for a domain (paginated)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|True|Domain name to query historical WHOIS for|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
|whois|string|historical|True|Must be set to historical|None|historical|None|None|
  
Example input:

```
{
  "domainName": "example.com",
  "format": "json",
  "page": 1,
  "whois": "historical"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]object|False|List of historical WHOIS records|None|
  
Example output:

```
{
  "response": [
    {}
  ]
}
```

#### IP Geolocation

This action is used to retrieve geolocation data for an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ipAddress|string|None|True|IPv4 or IPv6 address to geolocate|None|8.8.8.8|None|None|
  
Example input:

```
{
  "ipAddress": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|IP geolocation record|None|
  
Example output:

```
{
  "response": {}
}
```

#### IP Reputation

This action is used to retrieve the reputation score and risk assessment for an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ipAddress|string|None|True|IPv4 or IPv6 address to check|None|8.8.8.8|None|None|
  
Example input:

```
{
  "ipAddress": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|IP reputation record|None|
  
Example output:

```
{
  "response": {}
}
```

#### IP Security

This action is used to retrieve security intelligence for an IP address (threats, proxies, VPN, TOR)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ipAddress|string|None|True|IPv4 or IPv6 address to check|None|8.8.8.8|None|None|
  
Example input:

```
{
  "ipAddress": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|IP security record|None|
  
Example output:

```
{
  "response": {}
}
```

#### IP WHOIS

This action is used to perform a WHOIS lookup for an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|ipAddress|string|None|True|IPv4 or IPv6 address to query|None|8.8.8.8|None|None|
  
Example input:

```
{
  "format": "json",
  "ipAddress": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|IP WHOIS record|None|
  
Example output:

```
{
  "response": {}
}
```

#### Live WHOIS

This action is used to perform a live WHOIS lookup for a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|True|Domain name to query|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
  
Example input:

```
{
  "domainName": "example.com",
  "format": "json"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|WHOIS record|None|
  
Example output:

```
{
  "response": {}
}
```

#### Reverse DNS

This action is used to reverse DNS lookup by record value (IP, mail server, CNAME target, or NS name)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|exact|boolean|False|False|Match exactly (true) or partially (false)|None|False|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
|type|string|None|True|DNS record type to reverse search|["a", "aaaa", "mx", "cname", "ns", "txt", "soa"]|a|None|None|
|value|string|None|True|Record value to reverse search (IP, hostname, etc)|None|8.8.8.8|None|None|
  
Example input:

```
{
  "exact": false,
  "format": "json",
  "page": 1,
  "type": "a",
  "value": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]object|False|List of matching reverse DNS records|None|
  
Example output:

```
{
  "response": [
    {}
  ]
}
```

#### Reverse WHOIS

This action is used to find domains sharing a WHOIS attribute (keyword, email, owner, or company) - at least one 
criteria field is required

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|company|string|None|False|Company name to search for in WHOIS records|None|Example Inc|None|None|
|email|string|None|False|Email address to search for in WHOIS records (supports exact or regex)|None|user@example.com|None|None|
|exact|boolean|False|False|Match exactly (true) or partially (false)|None|True|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|keyword|string|None|False|Domain keyword to search for in WHOIS records|None|example|None|None|
|mode|string|default|False|Result detail level|["mini", "default"]|default|None|None|
|owner|string|None|False|Owner name to search for in WHOIS records|None|John Doe|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
|whois|string|reverse|True|Must be set to reverse|None|reverse|None|None|
  
Example input:

```
{
  "company": "Example Inc",
  "email": "user@example.com",
  "exact": false,
  "format": "json",
  "keyword": "example",
  "mode": "default",
  "owner": "John Doe",
  "page": 1,
  "whois": "reverse"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]object|False|List of matching WHOIS records|None|
  
Example output:

```
{
  "response": [
    {}
  ]
}
```

#### SSL Lookup

This action is used to retrieve live SSL certificate information for a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|chain|boolean|False|False|Include full certificate chain in the response|None|False|None|None|
|domainName|string|None|True|Domain name to retrieve SSL certificate for|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|sslRaw|boolean|False|False|Include raw PEM certificate in the response|None|False|None|None|
  
Example input:

```
{
  "chain": false,
  "domainName": "example.com",
  "format": "json",
  "sslRaw": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|SSL certificate record|None|
  
Example output:

```
{
  "response": {}
}
```

#### Subdomains

This action is used to retrieve subdomains for a domain (paginated, filterable by date and status)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|after|string|None|False|Optional YYYY-MM-DD lower bound on record date|None|2026-01-01|None|None|
|before|string|None|False|Optional YYYY-MM-DD upper bound on record date|None|2026-12-31|None|None|
|domainName|string|None|True|Base domain to enumerate subdomains for|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
|status|string|None|False|Optional subdomain status filter|None|active|None|None|
  
Example input:

```
{
  "after": "2026-01-01",
  "before": "2026-12-31",
  "domainName": "example.com",
  "format": "json",
  "page": 1,
  "status": "active"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]object|False|List of subdomains|None|
  
Example output:

```
{
  "response": [
    {}
  ]
}
```

#### Typosquatting

This action is used to find typosquatting variants of a keyword (paginated)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|keyword|string|None|True|Keyword or brand name to search typosquatting variants for|None|example|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
  
Example input:

```
{
  "format": "json",
  "keyword": "example",
  "page": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|[]object|False|List of typosquatting variants|None|
  
Example output:

```
{
  "response": [
    {}
  ]
}
```
### Triggers


#### Newly Registered Domains

This trigger is used to poll a newly-registered-domain stream. Select the TLD family to determine the API path, and set
 WHOIS to choose headerless (false) or header-on-every-page (true) CSV mode

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|batch_size|integer|500|True|Number of rows per emitted batch (controls the limit parameter)|None|500|None|None|
|date|string|None|False|Optional YYYY-MM-DD backfill seed. Must be between available_from and last_update for the feed. Once this date is fully ingested, the trigger automatically continues with the latest date reported by the status endpoint. Intermediate dates between the seed and the latest are not backfilled. Omit to start from the latest date immediately|None|2026-09-14|None|None|
|poll_interval_minutes|integer|60|True|Minutes to sleep between status checks after finishing a date|None|60|None|None|
|tld_family|string|None|True|Selects the stream path (gtld, cctld, cleaned_gtld, cleaned_cctld, or dns)|["gtld", "cctld", "cleaned_gtld", "cleaned_cctld", "dns"]|gtld|None|None|
|whois|boolean|False|True|False = headerless CSV pages; true = header on every page|None|False|None|None|
  
Example input:

```
{
  "batch_size": 500,
  "date": "2026-09-14",
  "poll_interval_minutes": 60,
  "tld_family": "gtld",
  "whois": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]object|False|Batched rows from the stream|None|
|next_offset|integer|False|Offset to resume from on the next run|0|
  
Example output:

```
{
  "events": [
    {}
  ],
  "next_offset": 0
}
```

#### Threat Feed

This trigger is used to poll a WhoisFreaks threat feed (phishing, malware, or spam)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|batch_size|integer|500|True|Number of rows per emitted batch (controls the limit parameter)|None|500|None|None|
|date|string|None|False|Optional YYYY-MM-DD backfill seed. Must be between available_from and last_update for the feed. Once this date is fully ingested, the trigger automatically continues with the latest date reported by the status endpoint. Intermediate dates between the seed and the latest are not backfilled. Omit to start from the latest date immediately|None|2026-09-14|None|None|
|poll_interval_minutes|integer|60|True|Minutes to sleep between status checks after finishing a date|None|60|None|None|
|threat_type|string|None|True|Which threat feed to poll|["phishing", "malware", "spam"]|phishing|None|None|
  
Example input:

```
{
  "batch_size": 500,
  "date": "2026-09-14",
  "poll_interval_minutes": 60,
  "threat_type": "phishing"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]object|False|Batched rows from the stream|None|
|next_offset|integer|False|Offset to resume from on the next run|0|
  
Example output:

```
{
  "events": [
    {}
  ],
  "next_offset": 0
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting


# Version History

* 1.0.0 - Initial plugin

# Links

* [WhoisFreaks](https://www.whoisfreaks.com)

## References

* {'name': 'WhoisFreaks NRD', 'url': 'https://whoisfreaks.com/products/newly-registered-domains'}
* {'name': 'Threat Feeds', 'url': 'https://whoisfreaks.com/products/threat-intelligence-feed'}
* {'name': 'WhoisFreaks API Documentation', 'url': 'https://whoisfreaks.com/documentation'}