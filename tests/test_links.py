from __future__ import annotations

import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import telegram_media_downloader as downloader


class ParsePostUrlTests(unittest.TestCase):
    def test_public_post(self) -> None:
        post = downloader.parse_post_url(
            "https://t.me/ExampleChannel/37?single"
        )
        self.assertEqual(post.channel_label, "ExampleChannel")
        self.assertEqual(post.entity, "ExampleChannel")
        self.assertEqual(post.message_id, 37)
        self.assertIsNone(post.comment_id)

    def test_comment_link(self) -> None:
        post = downloader.parse_post_url(
            "https://t.me/channel/737?single&comment=7145"
        )
        self.assertEqual(post.channel_label, "channel")
        self.assertEqual(post.message_id, 737)
        self.assertEqual(post.comment_id, 7145)

    def test_private_channel(self) -> None:
        post = downloader.parse_post_url(
            "https://t.me/c/1234567890/321"
        )
        self.assertEqual(post.channel_label, "channel_1234567890")
        self.assertEqual(post.entity, -1001234567890)
        self.assertEqual(post.message_id, 321)

    def test_rejects_untrusted_host(self) -> None:
        with self.assertRaisesRegex(ValueError, "只支持"):
            downloader.parse_post_url(
                "https://example.com/ExampleChannel/37"
            )

    def test_rejects_invalid_comment_id(self) -> None:
        with self.assertRaisesRegex(ValueError, "无效的评论编号"):
            downloader.parse_post_url(
                "https://t.me/ExampleChannel/37?comment=hello"
            )


if __name__ == "__main__":
    unittest.main()
