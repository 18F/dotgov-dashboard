# Accessibility

## Background

Pulse is embarking on scanning web accessibility using a tool called [`pa11y`](http://pa11y.org/). `pa11y` takes a URL, and uses another tool, called the [HTML Code Sniffer](https://squizlabs.github.io/HTML_CodeSniffer/), to analyze adherence to one of several web accessibility standards:

- Section 508
- WCAG 2.0 A
- WCAG 2.0 AA
- WCAG 2.0 AAA

Athough automated accessibility testing tools such as `pa11y` should likely not be used to outright determine compliance with accessibility regulations, the results reported by `pa11y` serve as an excellent set of diagnostics to aid in the process of ensuring web accessibility. The reports should help web managers, developers, and accessibility experts catch and fix accessibility bugs.

## Approach

For Pulse, `pa11y` will be checking .gov websites against the WCAG 2.0 AA Standard. This is the standard that the Access Board has signaled will become incorporated into Section 508 (see http://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-ict-refresh/preliminary-regulatory-impact-analysis). In the future, Pulse may scan against additional standards.

### Eligibility

[]

### Data Dictionary

This is a brief explaination of the data fields returned by the `pa11y` via the HTML Code Sniffer.

## Sample

```javascript
[
  {
    "code":"WCAG2AA.Principle2.Guideline2_4.2_4_2.H25.2",
    "context":"<title>18F Digital Services Delivery</title>",
    "message":"Check that the title element describes the document.",
    "selector":"html > head > title",
    "type":"notice",
    "typeCode":3
  }
]
```

- **"code"** - The Accessibility section in which the error, notice, or warning is derived
  - [WCAG2AA](http://www.w3.org/TR/WCAG20/)
  - [508](http://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-section-508-standards/section-508-standards)
- **"context"** - The specific piece of HTML from the web page that the error, notice, or warning was found or relates to
- **"message"** - How the context relates to the section or how to check manually
 - **"notice"** - The tool is prompting the user of a possible error. This program is unable to properly test the compliance guideline, so further instructions are provided in context
 - **"warning"** - A possible error has been found. The program is reasonably sure, something is wrong, but requires a human to verify
 - **"error"** - An issue on the site has been found. Errors are the most sever type the program can assign and it is reserved for known issues
- **"selector"** - CSS selector that points to the affected HTML element
- **"type"** - The type of issue found by the tool
- **"typeCode"** - Corresponds to "type"
 - 3 = notice, 2 = warning, 1 = error

## Making sense of the results

The quickest way to make sense of a `pa11y` report is to look at the aggregate counts of notices, warnings, and errors. We hypothesize that an errors will rarely be false negatives. That is to say, an error reported by `pa11y` is highly likely to correspond to an actual error.

### Caveats

[]
