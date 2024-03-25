def main(s):
    s = s[1:-1].split('.')[:-1]
    for i in range(len(s)):
        s[i] = s[i].strip().split('|>')
        s[i][0] = s[i][0].strip()[7:]
        s[i][1] = s[i][1].strip()[:-3]
        s[i][0], s[i][1] = s[i][1], s[i][0]
        s[i] = tuple(s[i])
    return s


print(main('( <% loc iser |> edle_900 %>. <% loc atqu|>ritebi %>. <% loc indiar\n|> areed %>.<% loc veerqu |> geanre %>. )'))