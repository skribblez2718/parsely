# Parsely Utils Directory

## DIRECTORY PURPOSE
Utility modules for the Parsely project - a cybersecurity tool that extracts host and endpoint information from Burp Suite Proxy History XML exports and converts them to PlexTrac-compatible CSV format.

## WHEN TO ACCESS
- Working with utility functions for XML parsing, URL processing, or CSV generation
- Understanding core parsing logic and data transformation
- Debugging data extraction or formatting issues
- Extending or modifying parsing capabilities

## MODULE DESCRIPTIONS

### asset.py
**PURPOSE**: Asset extraction and processing logic
**FUNCTIONALITY**:
- Extracts parent assets (hosts/IPs) from Burp XML data
- Extracts child assets (HTTP endpoints) with method and path information
- Formats asset data for CSV output with proper PlexTrac structure
- Handles filtering of invalid methods and paths

### csv.py
**PURPOSE**: CSV file generation for PlexTrac import
**FUNCTIONALITY**:
- Defines PlexTrac-compatible CSV column structure (20 columns)
- Converts asset tuples to CSV format
- Writes formatted data to output files
- Ensures proper CSV formatting with headers and data rows

### general.py
**PURPOSE**: General utility functions and argument parsing
**FUNCTIONALITY**:
- Command-line argument parsing (input XML, output CSV paths)
- Pattern matching for filenames, UUIDs, hex identifiers, numeric identifiers
- Helper functions for identifying different data types
- Error handling and validation utilities

### logger.py
**PURPOSE**: Centralized logging configuration
**FUNCTIONALITY**:
- Configures colored console logging using colorlog
- Sets up different log levels with color coding
- Provides consistent logging interface across all modules
- Enables debugging and monitoring of parsing operations

### url.py
**PURPOSE**: URL and path processing utilities
**FUNCTIONALITY**:
- Validates and filters HTTP methods (excludes OPTIONS)
- Detects and filters invalid paths (encoded URLs, files)
- Parameterizes URLs by replacing identifiers with placeholders
- Processes query parameters for consistent endpoint representation
- Filters out security testing artifacts (prototype pollution, etc.)

### xml.py
**PURPOSE**: XML parsing and data extraction
**FUNCTIONALITY**:
- Parses Burp Suite XML export files
- Extracts in-scope items from proxy history
- Provides XML tree traversal utilities
- Handles XML parsing errors and validation

## SECURITY CONTEXT
This is a defensive cybersecurity tool that:
- Processes Burp Suite proxy history exports (legitimate security testing data)
- Extracts asset information for vulnerability management platforms
- Helps organize and import security testing results
- Does not contain any offensive capabilities or malicious functionality

## INTEGRATION PATTERNS
- All modules use centralized logging from logger.py
- Error handling is consistent across modules with try/catch blocks
- Data flows: XML → asset extraction → CSV formatting → file output
- Modular design allows for easy testing and maintenance of individual components