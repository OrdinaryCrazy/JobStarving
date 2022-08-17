class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def log_key(log):
            log_id, content = log.split(" ", 1)
            return (0, content, log_id) if content[0].isalpha() else(1,)
        logs.sort(key=log_key)
        return logs
        #-----------------------------------------------------------------------
        # l_logs = []
        # d_logs = []
        # for log in logs:
        #     log_list = log.split(" ")
        #     if "0" <= log_list[1][0] and log_list[1][0] <= "9":
        #         d_logs.append(log)
        #     else:
        #         l_logs.append(log)
        # l_logs.sort(key=lambda x:(x.split(" ", 1)[1], x.split(" ", 1)[0]))
        # return l_logs + d_logs