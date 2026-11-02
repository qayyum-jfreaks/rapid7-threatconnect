# Description

WhoisFreaks (https://www.whoisfreaks.com) Unleash the Power of Data with Our Domain and IP Intelligence Gain real-time DNS, domain, and IP intelligence to strengthen security, protect your brand, and drive smarter decisions with our advanced data platform.

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
|api_url|string|https://api.whoisfreaks.com|True|Base URL for lookup endpoints|None|https://api.whoisfreaks.com|None|None|
|base_url|string|https://files.whoisfreaks.com|True|Base URL for stream and status endpoints|None|https://files.whoisfreaks.com|None|None|

Example input:

```
{
  "api_key": "your_api_key_here",
  "api_url": "https://api.whoisfreaks.com",
  "base_url": "https://files.whoisfreaks.com"
}
```

## Technical Details

### Actions


#### ASN WHOIS

This action is used to perform a WHOIS lookup for an Autonomous System Number

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asn|string|None|True|Autonomous System Number (with or without "as" prefix)|None|AS15169|None|None|
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

#### DNS Lookup

This action is used to perform a live DNS lookup for a domain or IP address. At least one of domainName or ipAddress is
 required.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|False|Domain name for DNS lookup|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|ipAddress|string|None|False|IP address for reverse DNS (PTR) lookup|None|8.8.8.8|None|None|
|type|string|None|False|DNS record type (e.g. A, AAAA, MX, NS, TXT, all)|None|all|None|None|
  
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

#### Domain Reputation

This action is used to retrieve the threat score and reputation assessment for a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|True|Domain to assess (must contain at least one dot, max 253 characters)|None|example.com|None|None|
  
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

#### Historical WHOIS

This action is used to retrieve historical WHOIS records for a domain (paginated)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domainName|string|None|True|Domain name to query historical WHOIS for|None|example.com|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
|whois|string|historical|True|Must be set to "historical"|None|historical|None|None|
  
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

#### IP WHOIS

This action is used to perform a WHOIS lookup for an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|ip|string|None|True|IPv4 or IPv6 address to query|None|8.8.8.8|None|None|
  
Example input:

```
{
  "format": "json",
  "ip": "8.8.8.8"
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

#### Reverse WHOIS

This action is used to find domains sharing a WHOIS attribute (keyword, email, owner, or company). At least one 
criteria field is required.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|company|string|None|False|Company name to search for in WHOIS records|None|Example Inc|None|None|
|email|string|None|False|Email address to search for in WHOIS records (supports exact or regex)|None|admin@example.com|None|None|
|exact|string|false|False|Whether to match exactly (true) or partially (false)|["True", "False"]|true|None|None|
|format|string|json|False|Response format|["json", "xml"]|json|None|None|
|keyword|string|None|False|Domain keyword to search for in WHOIS records|None|example|None|None|
|mode|string|default|False|Result detail level|["mini", "default"]|default|None|None|
|owner|string|None|False|Owner name to search for in WHOIS records|None|John Doe|None|None|
|page|integer|None|False|Page number for paginated results|None|1|None|None|
|whois|string|reverse|True|Must be set to "reverse"|None|reverse|None|None|
  
Example input:

```
{
  "company": "Example Inc",
  "email": "admin@example.com",
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
### Triggers


#### Newly Registered Domains

This trigger is used to poll a newly-registered-domain stream. Select the TLD family to determine the API path, and set
 whois to choose headerless (false) or header-on-every-page (true) CSV mode.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|batch_size|integer|500|True|Number of rows per emitted batch (controls the limit parameter)|None|None|None|None|
|date|string|None|True|Required YYYY-MM-DD. Must fall between available_from and last_update for the selected TLD family.|None|2026-09-14|None|None|
|dedupe_window_days|integer|1|True|Suppress duplicate events seen within this window|None|None|None|None|
|max_rows_per_run|integer|50000|True|Cap on total rows fetched in a single trigger run|None|None|None|None|
|tld_family|string|None|True|Selects the stream path (gtld, cctld, cleaned_gtld, cleaned_cctld, or dns)|["gtld", "cctld", "cleaned_gtld", "cleaned_cctld", "dns"]|gtld|None|None|
|whois|boolean|False|True|false = headerless CSV pages; true = header on every page|None|None|None|None|
  
Example input:

```
{
  "batch_size": 500,
  "date": "2026-09-14",
  "dedupe_window_days": 1,
  "max_rows_per_run": 50000,
  "tld_family": "gtld",
  "whois": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]object|False|Batched rows from the stream|None|
|next_offset|integer|False|Offset to resume from on the next run|None|
  
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

This trigger is used to poll a WhoisFreaks threat feed (phishing, malware, or spam).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|batch_size|integer|500|True|Number of rows per emitted batch (controls the limit parameter)|None|None|None|None|
|date|string|None|True|Required YYYY-MM-DD. Must fall between available_from and last_update for the selected threat feed.|None|2026-10-12|None|None|
|dedupe_window_days|integer|1|True|Suppress duplicate events seen within this window|None|None|None|None|
|max_rows_per_run|integer|50000|True|Cap on total rows fetched in a single trigger run|None|None|None|None|
|threat_type|string|None|True|Which threat feed to poll|["phishing", "malware", "spam"]|phishing|None|None|
  
Example input:

```
{
  "batch_size": 500,
  "date": "2026-10-12",
  "dedupe_window_days": 1,
  "max_rows_per_run": 50000,
  "threat_type": "phishing"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]object|False|Batched rows from the stream|None|
|next_offset|integer|False|Offset to resume from on the next run|None|
  
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
  
*This plugin does not contain a version history.*

# Links

* [WhoisFreaks](https://www.whoisfreaks.com)

## References

* {'name': 'WhoisFreaks NRD', 'url': 'https://whoisfreaks.com/products/newly-registered-domains'}
* {'name': 'Threat Feeds', 'url': 'https://whoisfreaks.com/products/threat-intelligence-feed'}
* {'name': 'WhoisFreaks API Documentation', 'url': 'https://whoisfreaks.com/documentation'}