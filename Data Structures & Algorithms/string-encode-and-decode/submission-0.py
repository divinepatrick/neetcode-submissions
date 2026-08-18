class Solution:

    def encode(self, strs: List[str]) -> str:
        new_list = []
        for i in range(len(strs)):
            new_list.append(str(len(strs[i])).zfill(4) + strs[i])
        encoded_string = "".join(new_list)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        index = 0
        total_length = len(s)
        # Loop until we have passed the entire string
        while index < total_length:
            # 1. Grab the 4-byte delimiter
            delimiter_bytes = s[index: index + 4]
            # Convert the delimiter string into an integer size
            chunk_size = int(delimiter_bytes)
            # Move our index past the 4-byte delimiter
            index += 4

            # 2. Slice out the text chunk based on the size
            text_chunk = s[index: index + chunk_size]
            # Add the text to our list
            decoded_list.append(text_chunk)
            # Move our index past the text chunk to the next delimiter
            index += chunk_size
        return decoded_list