# junkshon src ipscan
Scans directories and files for IP addresses inside source code and/or configuration files. 

The program scans files and outputs to a JSON file, the JSON file can be read by the junkshon platform if it is uploaded.

# Requirements 
Requires python3 to run.
You will require the appropriate permissions to read the source code repo or configuration files. 

# Getting Started
1. To configure the programme you need to add your source code directory path into the source_directory keypair called "junkshon_ipscan.json".
2. You can also configure the out file name in the scan_output_file key/pair in the "junkshon_ipscan.json" JSON file.

```
{
    "source_directory": "/app/src/",
    "scan_output_file": "ipscan_1.json"
}
```

3. Once the file has been configured you can run the python program as follows, at the comment prompt enter: 

% python junkshon_ip_addr_scan.py

4. The program will scan files with specific extensions, the program will scan the text file using Regex to find pattern matches for IP addresses. 

5. The output of the scan will result in a JSON file with the following structure. Each file with a pattern matching an IP address is written to the file with the path to the soruce file and the IP addresses found. 

```
[
    {
        "filepath": "/app/startdev.sh",
        "result": [
            "127.0.0.1",
            "127.0.0.1",
            "127.0.0.1",
            "127.0.0.1"
        ]
    },
    {
        "filepath": "/app/express.js",
        "result": [
            "10.6.23.1",
            "10.6.23.2",
            "10.6.23.3"
        ]
    }
]
```

The resulting file can then be used to represent a overview of source files with IP address values. 

---

Some options that you can consider when using this script is to include it into your developed Pipeline to validate and report on violations for hardcoded IP addresses. 

--

To clone using HTTPS:

git clone https://github.com/junkshon/junkshon_src_ipscan.git 

Using SSH:

git clone git@github.com:junkshon/junkshon_src_ipscan.git

For further information you can raise a question via the Issues feature in GitHub.
