class�Solution:����def�majorityElement(self,�nums:�List[int])�->�int:��������freq�=�defaultdict(int)��������for�num�in�nums:������������freq[num]�+=�1��������for�num,�count�in�freq.items():������������if�count�>�len(nums)//2:����������������return�num