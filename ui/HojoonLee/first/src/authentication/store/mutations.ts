export interface AuthenticationMutations {
    isAuthenticated: boolean
}

// 여기선 단순히 얘가 인증 되었나 안되었나만 봄
const mutations: AuthenticationMutations = {
    isAuthenticated: false // 처음엔 당연히 false로 초기화
}

export default mutations