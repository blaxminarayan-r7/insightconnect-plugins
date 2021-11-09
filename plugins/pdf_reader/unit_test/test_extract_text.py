from unittest import TestCase
from komand_pdf_reader.actions.extract_text import ExtractText
from komand_pdf_reader.actions.extract_text.schema import Input, Output
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


class TestExtractText(TestCase):
    @parameterized.expand(
        [
            [
                "from_pdf",
                "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MOpf75Id/SA/hY/KIio5P+3qyCXysUi8y3xNvM8anviQvzeJj5kPiU/IJWrOWb9PfMl8xlnuf01TpbX9pKVy8T4mxd1ixBROG/hdv7MuufB8A6XNgAkKZW5kc3RyZWFtCmVuZG9iagoKOSAwIG9iago8PC9UeXBlL0ZvbnQvU3VidHlwZS9UcnVlVHlwZS9CYXNlRm9udC9CQUFBQUErTGliZXJhdGlvblNlcmlmCi9GaXJzdENoYXIgMAovTGFzdENoYXIgOQovV2lkdGhzWzc3NyAzODkgNDQzIDc3NyA1MDAgMjc3IDQ0MyAyNTAgMjc3IDUwMCBdCi9Gb250RGVzY3JpcHRvciA3IDAgUgovVG9Vbmljb2RlIDggMCBSCj4+CmVuZG9iagoKMTAgMCBvYmoKPDwvRjEgOSAwIFIKPj4KZW5kb2JqCgoxMSAwIG9iago8PC9Gb250IDEwIDAgUgovUHJvY1NldFsvUERGL1RleHRdCj4+CmVuZG9iagoKMSAwIG9iago8PC9UeXBlL1BhZ2UvUGFyZW50IDQgMCBSL1Jlc291cmNlcyAxMSAwIFIvTWVkaWFCb3hbMCAwIDU5NS4zMDM5MzcwMDc4NzQgODQxLjg4OTc2Mzc3OTUyOF0vR3JvdXA8PC9TL1RyYW5zcGFyZW5jeS9DUy9EZXZpY2VSR0IvSSB0cnVlPj4vQ29udGVudHMgMiAwIFI+PgplbmRvYmoKCjQgMCBvYmoKPDwvVHlwZS9QYWdlcwovUmVzb3VyY2VzIDExIDAgUgovTWVkaWFCb3hbIDAgMCA1OTUgODQxIF0KL0tpZHNbIDEgMCBSIF0KL0NvdW50IDE+PgplbmRvYmoKCjEyIDAgb2JqCjw8L1R5cGUvQ2F0YWxvZy9QYWdlcyA0IDAgUgovT3BlbkFjdGlvblsxIDAgUiAvWFlaIG51bGwgbnVsbCAwXQovTGFuZyhwbC1QTCkKPj4KZW5kb2JqCgoxMyAwIG9iago8PC9DcmVhdG9yPEZFRkYwMDU3MDA3MjAwNjkwMDc0MDA2NTAwNzI+Ci9Qcm9kdWNlcjxGRUZGMDA0QzAwNjkwMDYyMDA3MjAwNjUwMDRGMDA2NjAwNjYwMDY5MDA2MzAwNjUwMDIwMDAzNjAwMkUwMDM0PgovQ3JlYXRpb25EYXRlKEQ6MjAyMTExMDkxODAxNTgrMDEnMDAnKT4+CmVuZG9iagoKeHJlZgowIDE0CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwNjY4NyAwMDAwMCBuIAowMDAwMDAwMDE5IDAwMDAwIG4gCjAwMDAwMDAyMTQgMDAwMDAgbiAKMDAwMDAwNjg1NiAwMDAwMCBuIAowMDAwMDAwMjM0IDAwMDAwIG4gCjAwMDAwMDU4NTcgMDAwMDAgbiAKMDAwMDAwNTg3OCAwMDAwMCBuIAowMDAwMDA2MDczIDAwMDAwIG4gCjAwMDAwMDY0MDUgMDAwMDAgbiAKMDAwMDAwNjYwMCAwMDAwMCBuIAowMDAwMDA2NjMyIDAwMDAwIG4gCjAwMDAwMDY5NTUgMDAwMDAgbiAKMDAwMDAwNzA1MiAwMDAwMCBuIAp0cmFpbGVyCjw8L1NpemUgMTQvUm9vdCAxMiAwIFIKL0luZm8gMTMgMCBSCi9JRCBbIDxENzQ5QzJERTI3NTY4NEE2Q0ZBQzZGMjUxQTcwMjFGND4KPEQ3NDlDMkRFMjc1Njg0QTZDRkFDNkYyNTFBNzAyMUY0PiBdCi9Eb2NDaGVja3N1bSAvMEM5MTE5NjA5QkEwQTkyNDBGQkZDQzlEQzU1OUZFMjQKPj4Kc3RhcnR4cmVmCjcyMjcKJSVFT0YK",
                "sample text",
            ],
            [
                "from_pdf2",
                "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IG9iago8PC9UeXBlL0ZvbnQvU3VidHlwZS9UcnVlVHlwZS9CYXNlRm9udC9CQUFBQUErTGliZXJhdGlvblNlcmlmCi9GaXJzdENoYXIgMAovTGFzdENoYXIgMTIKL1dpZHRoc1s3NzcgNjEwIDUwMCA0NDMgNzc3IDUwMCAyNzcgNDQzIDI1MCA2MTAgMjc3IDI3NyAzODkgXQovRm9udERlc2NyaXB0b3IgMTAgMCBSCi9Ub1VuaWNvZGUgMTEgMCBSCj4+CmVuZG9iagoKMTMgMCBvYmoKPDwvRjEgMTIgMCBSCj4+CmVuZG9iagoKMTQgMCBvYmoKPDwvRm9udCAxMyAwIFIKL1Byb2NTZXRbL1BERi9UZXh0XQo+PgplbmRvYmoKCjEgMCBvYmoKPDwvVHlwZS9QYWdlL1BhcmVudCA3IDAgUi9SZXNvdXJjZXMgMTQgMCBSL01lZGlhQm94WzAgMCA1OTUuMzAzOTM3MDA3ODc0IDg0MS44ODk3NjM3Nzk1MjhdL0dyb3VwPDwvUy9UcmFuc3BhcmVuY3kvQ1MvRGV2aWNlUkdCL0kgdHJ1ZT4+L0NvbnRlbnRzIDIgMCBSPj4KZW5kb2JqCgo0IDAgb2JqCjw8L1R5cGUvUGFnZS9QYXJlbnQgNyAwIFIvUmVzb3VyY2VzIDE0IDAgUi9NZWRpYUJveFswIDAgNTk1LjMwMzkzNzAwNzg3NCA4NDEuODg5NzYzNzc5NTI4XS9Hcm91cDw8L1MvVHJhbnNwYXJlbmN5L0NTL0RldmljZVJHQi9JIHRydWU+Pi9Db250ZW50cyA1IDAgUj4+CmVuZG9iagoKNyAwIG9iago8PC9UeXBlL1BhZ2VzCi9SZXNvdXJjZXMgMTQgMCBSCi9NZWRpYUJveFsgMCAwIDU5NSA4NDEgXQovS2lkc1sgMSAwIFIgNCAwIFIgXQovQ291bnQgMj4+CmVuZG9iagoKMTUgMCBvYmoKPDwvVHlwZS9DYXRhbG9nL1BhZ2VzIDcgMCBSCi9PcGVuQWN0aW9uWzEgMCBSIC9YWVogbnVsbCBudWxsIDBdCi9MYW5nKHBsLVBMKQo+PgplbmRvYmoKCjE2IDAgb2JqCjw8L0NyZWF0b3I8RkVGRjAwNTcwMDcyMDA2OTAwNzQwMDY1MDA3Mj4KL1Byb2R1Y2VyPEZFRkYwMDRDMDA2OTAwNjIwMDcyMDA2NTAwNEYwMDY2MDA2NjAwNjkwMDYzMDA2NTAwMjAwMDM2MDAyRTAwMzQ+Ci9DcmVhdGlvbkRhdGUoRDoyMDIxMTEwOTE4MDEyNiswMScwMCcpPj4KZW5kb2JqCgp4cmVmCjAgMTcKMDAwMDAwMDAwMCA2NTUzNSBmIAowMDAwMDA3NDk1IDAwMDAwIG4gCjAwMDAwMDAwMTkgMDAwMDAgbiAKMDAwMDAwMDI0MyAwMDAwMCBuIAowMDAwMDA3NjY0IDAwMDAwIG4gCjAwMDAwMDAyNjMgMDAwMDAgbiAKMDAwMDAwMDQ1OSAwMDAwMCBuIAowMDAwMDA3ODMzIDAwMDAwIG4gCjAwMDAwMDA0NzkgMDAwMDAgbiAKMDAwMDAwNjYzMCAwMDAwMCBuIAowMDAwMDA2NjUxIDAwMDAwIG4gCjAwMDAwMDY4NDcgMDAwMDAgbiAKMDAwMDAwNzE5NiAwMDAwMCBuIAowMDAwMDA3NDA3IDAwMDAwIG4gCjAwMDAwMDc0NDAgMDAwMDAgbiAKMDAwMDAwNzkzOCAwMDAwMCBuIAowMDAwMDA4MDM1IDAwMDAwIG4gCnRyYWlsZXIKPDwvU2l6ZSAxNy9Sb290IDE1IDAgUgovSW5mbyAxNiAwIFIKL0lEIFsgPDcyMjc2RDYyN0Y5NDAwREQ1MzgzQzNCMjlFQzU2NTQxPgo8NzIyNzZENjI3Rjk0MDBERDUzODNDM0IyOUVDNTY1NDE+IF0KL0RvY0NoZWNrc3VtIC80NzFERUU3RjZBQzhGNENGMDZFMUFENzUyRTA1QzZCNQo+PgpzdGFydHhyZWYKODIxMAolJUVPRgo=",
                "Example Title text text textsample text",
            ],
        ]
    )
    def test_extract_text(self, name, content, expected):
        action = ExtractText()
        actual = action.run({Input.CONTENTS: content})
        expected = {Output.OUTPUT: expected}
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "non_file",
                "test",
                "The provided content is not from the PDF file.",
                "Please check that the input is correct and try again.",
            ],
            [
                "non_pdf_file",
                "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",
                "The provided content is not from the PDF file.",
                "Please check that the input is correct and try again.",
            ],
        ]
    )
    def test_extract_text_bad(self, name, content, cause, assistance):
        action = ExtractText()
        with self.assertRaises(PluginException) as e:
            action.run({Input.CONTENTS: content})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
